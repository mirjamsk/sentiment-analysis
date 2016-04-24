/*
 Each API call to fetch list of posts returns a JSON containing:
	- post count
	- links to fetch the previous and next pages of posts
	- list of results i.e list of JSON objects representing a post
 e.g. 
{
	count: 	  223968,
	next: 	  "http://localhost:8000/api/posts.json?limit=10&offset=20",
	previous: "http://localhost:8000/api/posts.json?limit=10&offset=10",
	results: [
	{
		id:    79726,
		detail_link: "http://localhost:8000/api/posts/79726.json",
		content: 	 "In honor of the 30th anniversary of Sup...",
		link: 		 "https://www.facebook.com/...",
		likes:  2702,
		shares:   90,
		comments: 43,
		real_sentiment: null,
		sentiment_api1_ol: {
			sentiment_stats: {
				negative:  2,
				positive: 10,
				neutral:  38,
				total: 	  50
			},
			sentiment_label: "neutral"
		},
		sentiment_api1_en: {...},
		...
	},
	...
}	
*/

$( function(){
 var PostListModule = (function(){
	var data = {
		currentPage:  1,
		lastPage:     1,
		postCount: 	  0,
		postPerPage: 10,	
		url: '/api/posts.json/',
		params: {
			page:  this.currentPage,
			limit: this.postPerPage
		}
	};

	var util = {
		$postListContainer : $('#post-list-container'),
		$postItemTemplate  : $('.post-list-item').clone(),
		$postPaginationContainer : $('#post-list-pagination'),

		clearPostList: function(){
			this.$postListContainer.empty();
		},
        populatePostList: function(response){
			$.each( response.results, function( index, post ) {
                var $postItem = util.createListItem(post);
                util.appendPostItem($postItem);
                $postItem.fadeIn('slow');
          	});
		},
		appendPostItem: function($postItem){
			this.$postListContainer.append($postItem);
		},
		createListItem: function(post){
			var tempListItem = this.$postItemTemplate.clone();
	        	tempListItem
	        		.find('.collapsible-header-text')
		        	.html(post.id);	        	
	        	tempListItem
	        		.find('.collapsible-body p')
		        	.html(post.content);
    			tempListItem
					.find('.material-icons')
					.addClass(post.real_sentiment);
		            
	        return tempListItem;
		},
		ajaxRequest: function(url, data, success_function) {
		    $.ajax({
		        url: url,
		        data: data,
		        method: 'GET',
		        dataType: 'json',
        		contentType: 'application/json; charset=utf-8',
		        success: success_function,
		        error: function(requestObject, error, errorThrown) {
		            console.log( "Error in post_list_module::Util::loadContent: " + errorThrown);
		        }
		    });
		}
	};

	var paginationAPI = {
		requestPage : function(page){
            data.currentPage = page;
			data.params.page = data.currentPage;
			util.clearPostList();
			util.ajaxRequest(data.url, data.params, util.populatePostList);
		},
		getNumberOfPages: function(){
			return data.lastPage;
		}
	};

	// initial setup
	(function(){
		util.ajaxRequest(data.url, data.params, function(response){
			data.postCount = response.count;
			data.lastPage = Math.ceil(data.postCount/data.postPerPage);
			util.clearPostList();
			util.populatePostList(response);

            util.$postPaginationContainer.materializePagination({
                align: 'center',
                lastPage: data.lastPage ,
                urlParameter:'post-page',
				useUrlParameters:   true,
                onClickCallback: paginationAPI.requestPage
            });

		});
	})();
	
	// Methods available for external use
	return paginationAPI;
})();



});