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
            deps: ['jquery', 'materialize-pagination.min' ],
        },
        'post-detail-module': {
            deps: ['jquery', 'google', 'materialize', 'url-parser', 'sentiment-pie-chart'],
        },
        'comment-list-module': {
            deps: ['jquery', 'materialize', 'url-parser'],
        }
    }

});


define(['jquery', 'post-list-module', 'post-detail-module', 'comment-list-module'],
    function ($) {
        console.log('loaded');

    }
);