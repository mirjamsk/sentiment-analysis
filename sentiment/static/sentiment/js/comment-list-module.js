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

$( function(){
 var CommentListModule = (function(){
	var data = {
            currentPost: -1,
            url: '/api/comments/by/',
            urlParam: 'post-id'
        };

	var util = {
		$currentApiChoice: $('#current-api-choice '),
		$postListContainer: $('#post-list-container'),
		$commentListContainer : $('#comment-list-container'),
		$commentItemTemplate  : $('.comment-list-item').clone(),
		currentAPI: 'api1_ol',
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
			util.$commentListContainer.find('.comment-APIs span').hide();
			console.log(api)
			switch(api) {
				case ("api1_ol"):
				{
					util.$commentListContainer.find('.api1_ol').show();
					util.$commentListContainer.find('.api1_ol span:first').show();
					break;
				}
				case ("api1_en"):
				{
					util.$commentListContainer.find('.api1_en').show();
					util.$commentListContainer.find('.api1_en span:first').show();
					break;
				}
				case ("api2_ol"):
				{
					util.$commentListContainer.find('.api2_ol').show();
					util.$commentListContainer.find('.api2_ol span:first').show();
					break;
				}
				case ("api2_en"):
				{
					util.$commentListContainer.find('.api2_en').show();
					util.$commentListContainer.find('.api2_en span:first').show();
					break;
				}
				case ("api3"):
				{
					util.$commentListContainer.find('.api3').show();
					util.$commentListContainer.find('.api3 span:first').show();
					break;
				}
				case ("api4"):
				{
					util.$commentListContainer.find('.api4').show();
					util.$commentListContainer.find('.api4 span:first').show();
					break;
				}
					default:
						console.log("I am in default showParticularAPI")

			}
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
	        		.find('.comment-content span:first')
		        	.html(comment.content);
				tempListItem
	        		.find('.comment-content-translated span:first')
		        	.html(comment.english_translation);
				tempListItem
	        		.find('.api1_ol span:first')
		        	.html(comment.sentiment_api1_ol).show();
				tempListItem
	        		.find('.api1_en span:first')
		        	.html(comment.sentiment_api1_en).hide();
				tempListItem
	        		.find('.api2_ol span:first')
		        	.html(comment.sentiment_api2_ol).hide();
				tempListItem
	        		.find('.api2_en span:first')
		        	.html(comment.sentiment_api2_en).hide();
				tempListItem
	        		.find('.api3 span:first')
		        	.html(comment.sentiment_api3).hide();
				tempListItem
	        		.find('.api4 span:first')
		        	.html(comment.sentiment_api4).hide();
				tempListItem
	        		.find('.comment-real-sentiment span')
		        	.html(comment.real_sentiment);
				tempListItem
	        		.find('.api1_ol').show();
				tempListItem
	        		.find('.api2_ol').hide();
				tempListItem
	        		.find('.api1_en').hide();
				tempListItem
	        		.find('.api2_en').hide();
				tempListItem
	        		.find('.api3').hide();
				tempListItem
	        		.find('.api4').hide();
				


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
					console.log("I am in success callback");
					util.clearCommentList();
					util.populateCommentList(response);
           		},
		        error: function(requestObject, error, errorThrown) {
		            console.log( "Error in comment_list_module::Util::loadContent: " + errorThrown);
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
            $('#api-dropdown-button').dropdown({ belowOrigin: true });
            $('#api-dropdown-choices').on('click', 'li', function() {
                util.showParticularAPIsentiment($(this).data('api').substr(10));
				util.currentAPI = $(this).data('api').substr(10);
            });
        };

	 var bindToggleCommentsListener = function(){
		$('#toggle-comments-button').click(function(){
				util.$commentListContainer.toggleClass('hide');
		});
	 };

	// initial setup
	(function(){
		bindPostListClickListener();
		bindToggleCommentsListener();
		bindApiDropdownClickListener();
		data.currentPost = util.getDefaultPostId();
		requestPost(util.parseUrl());
		util.showParticularAPIsentiment(util.currentAPI);
	})();
	 
})();



});