$(function() {
    PostDetailModule = (function() {
        var data = {
            currentPost: -1,
            url: '/api/posts/'
        };

        var util = {
            postSentimentTabs: [],
            $postListContainer: $('#post-list-container'),
            $postDetailContent: $('#post-detail-content'),
            chartOptions: {
                width:  400,
                height: 300,
                legend: {
                    position: 'right',
                    alignment: 'center'
                },
                pieHole: 0.4,
                pieSliceTextStyle: { color: 'black' },
                backgroundColor: { fill:'transparent' },
                colors: ['#CFD8DC', '#C8E6C9', '#BCAAA4']
            },

            createChartData: function(stats) {
                return {
                    "cols": [
                        { "id": "", "label": "Sentiment", "pattern": "", "type": "string" },
                        { "id": "", "label": "Count", "pattern": "", "type": "number" }
                    ],
                    "rows": stats.total === 0 ? 
                        [{ "c": [{ "v": "0 comments", "f": null }, { "v": 1, "f": null }] }] : 
                        [{ "c": [{ "v": "neutral", "f": null }, { "v": stats.neutral, "f": null }] },
                        { "c": [{ "v": "positive", "f": null }, { "v": stats.positive, "f": null }] },
                        { "c": [{ "v": "negative", "f": null }, { "v": stats.negative, "f": null }] }]
                };
            },

            ajaxRequest: function(url, success_function) {
                $.ajax({
                    url: url,
                    method: 'GET',
                    dataType: 'json',
                    contentType: 'application/json; charset=utf-8',
                    success: success_function,
                    error: function(requestObject, error, errorThrown) {
                        console.log("Error in post_detail_module::Util::loadContent: " + errorThrown);
                    }
                });
            }
        };

        var clearPostDetail = function() {
            util.$postDetailContent.empty();
        };

        var loadPostDetails = function(response) {
            clearPostDetail();
            util.$postDetailContent.html(JSON.stringify(response.content));

            for (var i in util.postSentimentTabs) {
                var chartWrapper = util.postSentimentTabs[i].chartWrapper;
                var $sentimentTab = util.postSentimentTabs[i].$sentimentTab;
                var sentimentApiId = $sentimentTab.attr('id');
                var sentiment_stats = response[sentimentApiId].sentiment_stats;

                chartWrapper.setDataTable(util.createChartData(sentiment_stats));
                chartWrapper.draw();
            }
        };

        var requestPost = function(requestedPost) {
            if (data.currentPost === requestedPost) return;
            data.currentPost = requestedPost;
            util.ajaxRequest(data.url + data.currentPost + '.json/', loadPostDetails);
        };
        var bindClickEvent = function() {
            util.$postListContainer.on('click', 'li', function() {
                var requestedPost = parseInt($(this).data('post-id'));
                requestPost(requestedPost);
            });
        };

        var getChartWrapper = function(dataTable, containerId) {
            return new google.visualization.ChartWrapper({
                containerId: containerId,
                chartType: 'PieChart',
                dataTable:  dataTable,
                options: util.chartOptions,
            });
        };

        (function() {
            bindClickEvent();
            google.charts.load('current', { 'packages': ['corechart'] });

            var $stats = $('.sentiment-stats');

            google.charts.setOnLoadCallback(function() {

                $('#post-sentiment-tabs').children().each(function() { // init a pie chart for each snetiment api
                    $sentimentTab = $(this);
                    var chart_id = 'chart_' + $sentimentTab.attr('id');
                    var $chart = 
                        $stats.clone()
                        .attr('id', chart_id);

                    $sentimentTab.append($chart);
                    var chartWrapper = getChartWrapper(util.createChartData({ 'positive': 20, 'neutral': 14, 'negative': 8 }), chart_id);
                    
                    util.postSentimentTabs.push({
                        $sentimentTab: $sentimentTab,
                        chartWrapper: chartWrapper
                    });
                    requestPost($('#post-list-container').find('li:first-child').data('post-id'));
                });
            });
        })();
    })();
});
