
var urlParser = (function () {

    var getUrlParamByName = function (name) {
        name = name.replace(/[\[\]]/g, "\\$&");
        var url = window.location.href;
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
        var results = regex.exec(url);
        if (!results)  return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    };

    var updateUrlParam = function (key, value) {
        var urlQueryString = document.location.search;
        var newParam = key + '=' + value;
        var params = '?' + newParam;

        if (urlQueryString) { // If the "search" string exists, then build params from it
            keyRegex = new RegExp('([\?&])' + key + '[^&]*');

            if (urlQueryString.match(keyRegex) !== null) { // If param exists already, update it
                params = urlQueryString.replace(keyRegex, "$1" + newParam);
            }
            else { // Otherwise, add it to end of query string
                params = urlQueryString + '&' + newParam;
            }
        }
        window.history.pushState('', '', params);
    };

    return {
        getUrlParamByName: getUrlParamByName,
        updateUrlParam: updateUrlParam
    };
});
