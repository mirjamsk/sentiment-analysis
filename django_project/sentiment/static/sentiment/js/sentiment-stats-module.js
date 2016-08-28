
var SentimentStatsModule = (function() {
    var instance;
    var util = {
        postRealSentimentPieChart: null,
        postSentimentTabs: [],
        $currentApiChoice: $('#current-api-choice '),
        $sentimentApiTabs: $('#post-sentiment-stats ul.tabs'),
        prettify: function(api){
            return api.split('sentiment_')[1].replace('_', ' ').toUpperCase();
        }
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

    var populateDropdownAndTabs = function (sentimentLabels) {
        var $tabLinks = $('#post-sentiment-tab-links');
        var $dropdown = $('#api-dropdown-choices');
        var $tabs = $('#post-sentiment-tabs');

        sentimentLabels.sentimentAPIs.forEach(function (api) {
            $dropdown.append($('<li>')          // e.g. <li data-api="sentiment_api4"> <a>API 4</a> </li>
                .attr('data-api', api)
                .append($('<a>').html(util.prettify(api))));
            
            $tabLinks.append($('<li>')          // e.g <li class="tab col s2"><a href="#sentiment_api4">API 4</a></li>
                .addClass('tab col s2')
                .append($('<a>').attr('href', '#' + api).html(util.prettify(api))));
           
            $tabs.append($('<div>')             // e.g  <div id="sentiment_api1_ol" class="col s12"></div>
                .addClass('col s12')
                .attr('id', api));
        });
        $tabLinks.tabs('select_tab', sentimentLabels.defaultAPI);
    };

    var init = function (sentimentLabels) {
        populateDropdownAndTabs(sentimentLabels);
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
        redrawSentimentStats: redrawSentimentStats,
        init: function(sentimentLabels) {
            if (!instance) {
                instance = init(sentimentLabels);
            }
        }
    };

})();
