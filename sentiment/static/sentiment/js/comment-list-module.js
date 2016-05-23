/*
 Each API call to fetch list of comments filtered by idpost returns a JSON containing:
	- list of results i.e list of JSON objects representing a comment
 e.g.
[
    {
        "id": 645,
        "language": "it",
        "content": "Se venite a casa mia ve regalo il GameBoy con la cassetta di Super Mario e fate prima.",
        "english_translation": "If you come to my house you gift GameBoy with the cassette of Super Mario and make first.",
        "real_sentiment": null,
        "sentiment_api1_ol": "positive",
        "sentiment_api1_en": "positive",
        "sentiment_api2_ol": "positive",
        "sentiment_api2_en": "positive",
        "sentiment_api3": "neutral",
        "sentiment_api4": "positive",
        "idpost": "http://localhost:8000/api/posts/79726/",
        "detail_link": "http://localhost:8000/api/comments/645/"
    },
    {
        "id": 646,
        "language": "en",
        "content": "The Barbie collection was the best!",
        "english_translation": "The Barbie collection was the best!",
        "real_sentiment": null,
        "sentiment_api1_ol": "positive",
        "sentiment_api1_en": "positive",
        "sentiment_api2_ol": "positive",
        "sentiment_api2_en": "positive",
        "sentiment_api3": "positive",
        "sentiment_api4": "positive",
        "idpost": "http://localhost:8000/api/posts/79726/",
        "detail_link": "http://localhost:8000/api/comments/646/"
    },....
]
*/

 var CommentListModule = (function(){
    var instance;
	var data = {
            currentPost: -1,
            url: '/api/comments/by/',
            urlParam: 'post-id',
			currentAPI: '',
			sentimentLabels: []
        };

	var util = {
		$commentNumber: $('#toggle-comment-nb'),
		$currentApiChoice: $('#current-api-choice '),
		$postListContainer: $('#post-list-container'),
		$commentListContainer : $('#comment-list-container'),
		$commentItemTemplate  : $('.comment-list-item').clone(),
		urlParser: urlParser() || null,

		getDefaultPostId: function() {
                return parseInt(this.$postListContainer.find('li:first-child').data('post-id'));
		},
		sanitizePostRequest: function(requestedPost) {
			requestedPost = isNaN(requestedPost) ?
				this.getDefaultPostId() : parseInt(requestedPost);
                this.urlParser.updateUrlParam(data.urlParam, requestedPost);
                return requestedPost;
		},
		parseUrl: function() {
			var requestedPost = this.urlParser.getUrlParamByName(data.urlParam) || data.currentPost;
			return this.sanitizePostRequest(requestedPost);
		},
		showParticularAPIsentiment: function(api){
			util.$commentListContainer.find('.comment_' + data.currentAPI).hide();
			util.$commentListContainer.find('.comment_' + api).show();
		},
		clearCommentList: function(){
			this.$commentListContainer.empty();
		},
        populateCommentList: function(response){
			$.each( response, function( index, comment ) {
                var $commentItem = util.createListItem(comment);
                util.appendCommentItem($commentItem);
				$commentItem.fadeIn('slow');
          	});
		},
		appendCommentItem: function($commentItem){
			this.$commentListContainer.append($commentItem);
		},
		createListItem: function(comment){
			var tempListItem = this.$commentItemTemplate.clone();
				tempListItem.attr('data-comment-id', comment.id);
	        	tempListItem
	        		.find('.header-text')
		        	.html(comment.id);
				tempListItem
	        		.find('a.comment-api-link')
		        	.attr('href', comment.detail_link.split('.json')[0]);
	        	tempListItem
	        		.find('#comment-content-ol span')
		        	.html(comment.content);
				tempListItem
	        		.find('#comment-content-translated')
		        	.html(comment.english_translation);
			    tempListItem
	        		.find('.comment_' + data.sentimentLabels.realSentiment + ' span')
		        	.html(comment[data.sentimentLabels.realSentiment]);
				data.sentimentLabels.sentimentAPIs.forEach(function(api) {
				    tempListItem
	        		.find('.comment_' + api + ' span')
		        	.html(comment[api]);
				});
	        return tempListItem;
		}
	};
	 
	 var requestPost = function(requestedPost) {
            if (data.currentPost === requestedPost) return;
            data.currentPost = requestedPost;
		 	$.ajax({
		        url: data.url + requestedPost + '.json/',
		        data: data,
		        method: 'GET',
		        dataType: 'json',
        		contentType: 'application/json; charset=utf-8',
		        success: function(response){
					var commentNb = Object.keys(response).length;
					util.$commentNumber.html(commentNb + (commentNb == 1 ? ' comment' : ' comments'));
					data.currentAPI = data.sentimentLabels.defaultAPI;
					util.clearCommentList();
					util.populateCommentList(response);
					util.showParticularAPIsentiment(data.currentAPI);

           		},
		        error: function(requestObject, error, errorThrown) {
		            console.log( "Error in comment_list_module::requestPost: " + errorThrown);
		        }
		    });
        };

	 var bindPostListClickListener = function() {
            util.$postListContainer.on('click', 'a', function() {
                var requestedPost = util.sanitizePostRequest($(this).data('post-id'));
                requestPost(requestedPost);
            });
        };

	 var bindApiDropdownClickListener = function() {
            $('#api-dropdown-choices').on('click', 'li', function() {
				var requestedApi = $(this).data('api');
                util.showParticularAPIsentiment(requestedApi );
				data.currentAPI = requestedApi ;
            });
        };

	 var bindToggleCommentsListener = function(){
		 var $toggleArrow =$('#toggle-comments-button i');
		$('#toggle-comments-button').click(function(){
			util.$commentListContainer.slideToggle(150, 'linear');
			$toggleArrow.toggleClass('rotate-up, rotate-down');
		});
	 };

	// initial setup
	var init = function(sentimentLabels){
		data.sentimentLabels = sentimentLabels;
		bindPostListClickListener();
		bindToggleCommentsListener();
		bindApiDropdownClickListener();
		data.currentPost = util.getDefaultPostId();
		requestPost(util.parseUrl());
		return this;
	};
	 return{
		init: function (sentimentLabels) {
      		if ( !instance ) {
        	instance = init(sentimentLabels);
      	}
    }
  };

})();
