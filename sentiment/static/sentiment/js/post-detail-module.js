$(function() {
    var PostDetailModule = (function() {
        var data = {
            currentPost: -1,
            url: '/api/posts/',
            urlParam: 'post-id'
        };

        var util = {
            postRealSentimentPieChart: null,
            postSentimentTabs: [],
            $currentApiChoice: $('#current-api-choice '),
            $sentimentApiTabs: $('#post-sentiment-stats ul.tabs'),
            $postListContainer: $('#post-list-container'),
            $errorContainer: $('#post-details .error-msg'),
            $postDetails: $('#post-details'),
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
            util.$postDetails.find('#post-id span').text(response.id).fadeIn('slow');
            util.$postDetails.find('#post-content').html(response.content).fadeIn('slow');
            util.$postDetails.find('#post-likes').text(response.likes).fadeIn('slow');
            util.$postDetails.find('#post-shares').text(response.shares).fadeIn('slow');
            util.$postDetails.find('#post-comment-nb').text(total_comments).fadeIn('slow');
            util.$postDetails.find('#post-link').attr('href', response.link);
            util.$postDetails.find('#post-api-link').attr('href', response.detail_link.replace('.json', '/'));

            util.postRealSentimentPieChart.setData(response.real_sentiment.sentiment_stats);
            util.postRealSentimentPieChart.draw();
            for (var i in util.postSentimentTabs) {
                var pieChart = util.postSentimentTabs[i].pieChart;
                var $sentimentTab = util.postSentimentTabs[i].$sentimentTab;
                var sentimentApiId = $sentimentTab.attr('id');
                var sentiment_stats = response[sentimentApiId].sentiment_stats;

                pieChart.setData(sentiment_stats);
                pieChart.draw();
            }
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

        var bindApiDropdownClickListener = function() {
            $('#api-dropdown-button').dropdown({ belowOrigin: true });
            $('#api-dropdown-choices').on('click', 'li', function() {
                util.$sentimentApiTabs.tabs('select_tab', $(this).data('api'));
                util.$currentApiChoice.text($(this).data('api').replace(/sentiment|_|(\d)/g, ' $1'));
            });
        };

        (function() {
            bindPostListClickListener();
            bindApiDropdownClickListener();
            data.currentPost = util.getDefaultPostId();

            google.charts.load('current', { 'packages': ['corechart'] });
            google.charts.setOnLoadCallback(function() {

                requestPost(util.parseUrl());
                util.postRealSentimentPieChart = new SentimentPieChart({ 'total': 0 }, 'post-real-sentiment-chart');

                $('#post-sentiment-tabs').children().each(function() { // init a pie chart for each snetiment api tab
                    var $sentimentTab = $(this);
                    var chart_id = 'chart_' + $sentimentTab.attr('id');

                    $sentimentTab.append(
                        $('<div>')
                        .attr('id', chart_id)
                        .addClass('sentiment-stats'));

                    util.postSentimentTabs.push({
                        $sentimentTab: $sentimentTab,
                        pieChart: new SentimentPieChart({ 'total': 0 }, chart_id)
                    });
                });
            });
        })();
    })();
});
