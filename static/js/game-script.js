$(function() {
    $('#work').click(function () {
        $('#work').hide();
        $('#sleep').show();
    });

    $('#sleep').click(function () {
        $('#sleep').hide();
        $('#work').show();
    });
    $('#talk').click(function () {
        $('#talk-select').show();
        $('#buy-select').hide();
        $('#food-select').hide();
    });
    $('#buy').click(function () {
        $('#talk-select').hide();
        $('#buy-select').show();
        $('#food-select').hide();
    });
    $('#feed').click(function () {
        $('#talk-select').hide();
        $('#buy-select').hide();
        $('#food-select').show();
    });
});