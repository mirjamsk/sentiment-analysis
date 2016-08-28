var SentimentPieChart = function(sentiment_stats, containerId) {

    var _chartOptions = {
        width: 320,
        height: 220,
        legend: {
            position:  'right',
            alignment: 'center'
        },
        chartArea: {
            width:  '80%',
            height: '100%'
        },
        pieHole: 0.4,
        pieSliceTextStyle: { color: 'black' },
        backgroundColor: { fill: 'transparent' },
        colors: ['#CFD8DC', '#C8E6C9', '#BCAAA4']
    };

    var _createChartData = function(stats) {
        return {
            "cols": [
                { "id": "", "label": "Sentiment", "pattern": "", "type": "string" },
                { "id": "", "label": "Count", "pattern": "", "type": "number" }],
            "rows": stats.total === 0 ? 
                [{ "c": [{ "v": "0 comments", "f": null }, { "v": 1, "f": null }] }] : 
                [{ "c": [{ "v": "neutral", "f": null }, { "v": stats.neutral, "f": null }] },
                { "c": [{ "v": "positive", "f": null }, { "v": stats.positive, "f": null }] },
                { "c": [{ "v": "negative", "f": null }, { "v": stats.negative, "f": null }] }]
        };
    };

    var _createChartWrapper = function(dataTable, containerId) {
        return new google.visualization.ChartWrapper({
            containerId: containerId,
            chartType: 'PieChart',
            dataTable: dataTable,
            options: _chartOptions,
        });
    };

    var _chartWrapper = _createChartWrapper(_createChartData(sentiment_stats), containerId);

    return {
        draw: function() { 
            _chartWrapper.draw(); 
        },setData: function(sentiment_stats) {
            _chartWrapper.setDataTable(_createChartData(sentiment_stats));
        }
    };
};
