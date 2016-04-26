$(function () {
    var PostDetailModule = (function () {
        var data = {
            currentPost: -1,
            url: '/api/posts/',
            urlParam: 'post-id'
        };

        var util = {
            urlParser: urlParser() || null,
            postSentimentTabs: [],
            $currentApiChoice: $('#current-api-choice '),
            $sentimentApiTabs: $('#post-sentiment-stats ul.tabs'),
            $postListContainer: $('#post-list-container'),
            $postDetailContent: $('#post-detail-content'),

            chartOptions: {
                width: 320,
                height: 220,
                legend: {
                    position: 'right',
                    alignment: 'center'
                },
                chartArea: {
                    width: '80%',
                    height: '100%'
                },
                pieHole: 0.4,
                pieSliceTextStyle: {color: 'black'},
                backgroundColor: {fill: 'transparent'},
                colors: ['#CFD8DC', '#C8E6C9', '#BCAAA4']
            },
            createChartData: function (stats) {
                return {
                    "cols": [
                        {"id": "", "label": "Sentiment", "pattern": "", "type": "string"},
                        {"id": "", "label": "Count", "pattern": "", "type": "number"}
                    ],
                    "rows": stats.total === 0 ?
                        [{"c": [{"v": "0 comments", "f": null}, {"v": 1, "f": null}]}] :
                        [{"c": [{"v": "neutral", "f": null}, {"v": stats.neutral, "f": null}]},
                         {"c": [{"v": "positive", "f": null}, {"v": stats.positive, "f": null}]},
                         {"c": [{"v": "negative", "f": null}, {"v": stats.negative, "f": null}]}]
                };
            },
            
            getDefaultPostId: function(){
                return parseInt(this.$postListContainer.find('li:first-child').data('post-id'));
            },
            sanitizePostRequest: function(requestedPost){
                requestedPost = isNaN(requestedPost) ? 
                    this.getDefaultPostId() : parseInt(requestedPost);
                this.urlParser.updateUrlParam(data.urlParam, requestedPost);  
                return requestedPost;
            },           
            parseUrl: function(){
                var requestedPost = this.urlParser.getUrlParamByName(data.urlParam) || data.currentPost;
                return this.sanitizePostRequest(requestedPost);
            },


            ajaxRequest: function (url, success_function) {
                $.ajax({
                    url: url,
                    method: 'GET',
                    dataType: 'json',
                    contentType: 'application/json; charset=utf-8',
                    success: success_function,
                    error: function (requestObject, error, errorThrown) {
                        if (requestObject.status === 404)
                            util.$postDetailContent.find('#post-content')
                            .html('<p class="error">Post '+data.currentPost + ' ' +requestObject.statusText+'</p>')
                            .fadeIn('slow');

                        console.error("Error in post_detail_module::Util::loadContent: " + errorThrown);
                    }
                });
            }
        };

        var clearPostDetail = function () {
            util.$postDetailContent.find('#post-id span').hide();
            util.$postDetailContent.find('#post-content').hide();
            util.$postDetailContent.find('#post-likes').hide();
            util.$postDetailContent.find('#post-shares').hide();
            util.$postDetailContent.find('#post-comment-nb').hide();
        };

        var loadPostDetails = function (response) {
            clearPostDetail();
            util.$postDetailContent.find('#post-id span').html(response.id).fadeIn('slow');
            util.$postDetailContent.find('#post-content').html(response.content).fadeIn('slow');
            util.$postDetailContent.find('#post-likes').text(response.likes).fadeIn('slow');
            util.$postDetailContent.find('#post-shares').text(response.shares).fadeIn('slow');
            util.$postDetailContent.find('#post-comment-nb').text(response.comments).fadeIn('slow');
            util.$postDetailContent.find('#post-link').attr('href', response.link);
            util.$postDetailContent.find('#post-api-link').attr('href', response.detail_link.replace('.json', '/'));

            for (var i in util.postSentimentTabs) {
                var chartWrapper = util.postSentimentTabs[i].chartWrapper;
                var $sentimentTab = util.postSentimentTabs[i].$sentimentTab;
                var sentimentApiId = $sentimentTab.attr('id');
                var sentiment_stats = response[sentimentApiId].sentiment_stats;

                chartWrapper.setDataTable(util.createChartData(sentiment_stats));
                chartWrapper.draw();
            }
        };


        var requestPost = function (requestedPost) {
            if (data.currentPost === requestedPost) return;
            data.currentPost = requestedPost;
            util.ajaxRequest(data.url + data.currentPost + '.json/', loadPostDetails);
        };

        var getChartWrapper = function (dataTable, containerId) {
            return new google.visualization.ChartWrapper({
                containerId: containerId,
                chartType: 'PieChart',
                dataTable: dataTable,
                options: util.chartOptions,
            });
        };

        var bindPostListClickListener = function () {
            util.$postListContainer.on('click', 'a', function () {
                var requestedPost = util.sanitizePostRequest($(this).data('post-id'));
                requestPost(requestedPost);
            });
        };
        
        var bindApiDropdownClickListener = function () {
            $('#api-dropdown-button').dropdown({belowOrigin: true});
            $('#api-dropdown-choices').on('click', 'li', function () {
                util.$sentimentApiTabs.tabs('select_tab', $(this).data('api'));
                util.$currentApiChoice.text($(this).data('api').replace(/_/g, ' '));
            });
        };

        (function () {
            bindPostListClickListener();
            bindApiDropdownClickListener();
            data.currentPost = util.getDefaultPostId();
            google.charts.load('current', {'packages': ['corechart']});
            google.charts.setOnLoadCallback(function () {
                requestPost(util.parseUrl());

                $('#post-sentiment-tabs').children().each(function () { // init a pie chart for each snetiment api
                    var $sentimentTab = $(this);
                    var chart_id = 'chart_' + $sentimentTab.attr('id');

                    $sentimentTab.append(
                        $('<div>')
                        .attr('id', chart_id)
                        .addClass('sentiment-stats'));

                    var chartWrapper = getChartWrapper(util.createChartData({'total': 0}), chart_id);
                    util.postSentimentTabs.push({
                        chartWrapper: chartWrapper,
                        $sentimentTab: $sentimentTab
                    });
                });
            });
        })();
    })();
});
