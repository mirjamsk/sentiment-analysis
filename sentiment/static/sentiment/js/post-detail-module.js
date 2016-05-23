
var PostDetailModule = (function() {
    var instance;
    var data = {
        currentPost: -1,
        url: '/api/posts/',
        urlParam: 'post-id'
    };

    var util = {
        postSentimentTabs: [],
        SentimentStatsModule: null,
        $postListContainer: $('#post-list-container'),
        $errorContainer: $('#post-details .error-msg'),
        $postDetails: $('#post-details'),
        urlParser: urlParser() || null,

        sanitizePostRequest: function(requestedPost) {
            requestedPost = isNaN(requestedPost) ?
                data.currentPost : parseInt(requestedPost);
            this.urlParser.updateUrlParam(data.urlParam, requestedPost);
            return requestedPost;
        },

        ajaxRequest: function(url, success_function) {
            $.ajax({
                url: url,
                method: 'GET',
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                success: success_function,
                error: function(requestObject, error, errorThrown) {
                    util.$postDetails.find('#post-id span').html(data.currentPost).fadeIn('slow');
                    util.$postDetails.find('.post-content').hide();
                    util.$errorContainer
                        .text(requestObject.statusText)
                        .fadeIn('slow');
                    console.error("Error in post_detail_module::Util::loadContent: " + errorThrown);
                }
            });
        }
    };

    var clearPostDetail = function() {
        if (util.$errorContainer.is(":visible")) {
            util.$errorContainer.fadeOut();
            util.$postDetails.find('.post-content').fadeIn();
        }
        util.$postDetails.find('#post-likes').hide();
        util.$postDetails.find('#post-shares').hide();
        util.$postDetails.find('#post-id span').hide();
        util.$postDetails.find('#post-content').hide();
        util.$postDetails.find('#post-comment-nb').hide();
    };

    var loadPostDetails = function(response) {
        clearPostDetail();
        var total_comments = response.sentiment_api4.sentiment_stats.total;
        util.SentimentStatsModule.redrawSentimentStats(response);
        util.$postDetails.find('#post-id span').text(response.id).fadeIn('slow');
        util.$postDetails.find('#post-content').html(response.content).fadeIn('slow');
        util.$postDetails.find('#post-likes').text(response.likes).fadeIn('slow');
        util.$postDetails.find('#post-shares').text(response.shares).fadeIn('slow');
        util.$postDetails.find('#post-comment-nb').text(total_comments).fadeIn('slow');
        util.$postDetails.find('#post-link').attr('href', response.link);
        util.$postDetails.find('#post-api-link').attr('href', response.detail_link.replace('.json', '/'));

    };

    var requestPost = function(requestedPost) {
        if (data.currentPost === requestedPost) return;
        data.currentPost = requestedPost;
        util.ajaxRequest(data.url + data.currentPost + '.json/', loadPostDetails);
    };

    var bindPostListClickListener = function() {
        util.$postListContainer.on('click', 'a', function() {
            var requestedPost = util.sanitizePostRequest($(this).data('post-id'));
            requestPost(requestedPost);
        });
    };

    var init = function(requestedPost, SentimentStatsModule) {
        util.SentimentStatsModule = SentimentStatsModule;
        bindPostListClickListener();
        requestPost(requestedPost);

    };

    return {
        init: function(requestedPost, SentimentStatsModule) {
            if (!instance) {
                instance = init(requestedPost, SentimentStatsModule);
            }
        }
    };

})();

