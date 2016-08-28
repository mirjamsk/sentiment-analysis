requirejs.config({
    baseUrl: 'static/sentiment/js/',
    paths: {
        jquery: 'libs/jquery-2.2.3.min',
        google: 'libs/google-charts',
        hammerjs: 'libs/hammer.min',
        materialize: 'libs/materialize.min',
    },
    shim: {
        'materialize': {
            deps: ['jquery', 'hammerjs']
        },
        'url-parser': {
            exports: 'urlParser'
        },
        'sentiment-pie-chart': {
            deps: ['google'],
            exports: 'SentimentPieChart'
        },
        'materialize-pagination.min': {
            deps: ['jquery', 'materialize'],
        },
        'post-list-module': {
            deps: ['jquery', 'materialize-pagination.min'],
        },
        'sentiment-stats-module': {
            deps: ['jquery', 'google', 'materialize', 'sentiment-pie-chart'],
        },
        'post-detail-module': {
            deps: ['jquery', 'url-parser', 'sentiment-stats-module'],  // TO-DO make the sentiment stats it's own module
        },
        'comment-list-module': {
            deps: ['jquery'],
        }
    }
});

require(['jquery', 'url-parser', 'post-list-module', 'post-detail-module', 'comment-list-module'], function ($, urlParser) {

    var urlParser = urlParser();
    var sentimentLabels = {
        realSentiment: 'real_sentiment',
        sentimentAPIs: [
            'sentiment_api1_ol',
            'sentiment_api1_en',
            'sentiment_api2_ol',
            'sentiment_api2_en',
            'sentiment_api3',
            'sentiment_api4'
        ],
        defaultAPI: 'sentiment_api1_ol'
    };

    var requestedPostPage = parseInt(urlParser.getUrlParamByName('post-page'));
    requestedPostPage = isNaN(requestedPostPage) || requestedPostPage < 0 ? 1 : requestedPostPage;
    var requestedPost = parseInt(urlParser.getUrlParamByName('post-id'));

    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(initModules);

    function initModules() {

        PostListModule.init(requestedPostPage, function (firstPostId) {

            requestedPost = isNaN(requestedPost) || requestedPost < 0 ? firstPostId : parseInt(requestedPost);
            urlParser.updateUrlParam('post-id', requestedPost);

            SentimentStatsModule.init(sentimentLabels);
            PostDetailModule.init(requestedPost, SentimentStatsModule, sentimentLabels);
            CommentListModule.init(requestedPost, sentimentLabels);
        });
    }

    $(document).ready(function () {
        $(".button-collapse").sideNav();
    })
});