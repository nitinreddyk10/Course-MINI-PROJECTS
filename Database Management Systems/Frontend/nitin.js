(function() {
    var width, height, largeHeader, canvas, ctx, target = true;
    initHeader();
    function initHeader() {
        width = window.innerWidth;
        height = window.innerHeight;
        target = {x: width/2, y: height/2};
        largeHeader = document.getElementById('large-header');
        largeHeader.style.height = height+'px';
    }
})();