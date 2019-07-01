(function () {
    const app = angular.module('app',[]);
    app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    window.app = app;
  });
})();