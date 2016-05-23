
var SentimentStatsModule = (function() {
    var instance;
    var util = {
        postRealSentimentPieChart: null,
        postSentimentTabs: [],
        $currentApiChoice: $('#current-api-choice '),
        $sentimentApiTabs: $('#post-sentiment-stats ul.tabs'),
    };

    var redrawSentimentStats = function(response) {
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

    var bindApiDropdownClickListener = function() {
        $('#api-dropdown-button').dropdown({ belowOrigin: true });
        $('#api-dropdown-choices').on('click', 'li', function() {
            util.$sentimentApiTabs.tabs('select_tab', $(this).data('api'));
            util.$currentApiChoice.text($(this).data('api').replace(/sentiment|_|(\d)/g, ' $1'));
        });
    };

    var init = function (sentimentLabels) {
        bindApiDropdownClickListener();
        util.postRealSentimentPieChart = new SentimentPieChart({'total': 0}, 'post-real-sentiment-chart');

        $('#post-sentiment-tabs').children().each(function () { // init a pie chart for each snetiment api tab
            var $sentimentTab = $(this);
            var chart_id = 'chart_' + $sentimentTab.attr('id');
            $sentimentTab.append(
                $('<div>')
                    .attr('id', chart_id)
                    .addClass('sentiment-stats'));

            util.postSentimentTabs.push({
                $sentimentTab: $sentimentTab,
                pieChart: new SentimentPieChart({'total': 0}, chart_id)
            });

        });
    };

    return {
        init: function(sentimentLabels) {
            if (!instance) {
                instance = init(sentimentLabels);
            }
        },
        redrawSentimentStats: redrawSentimentStats
    };

})();
