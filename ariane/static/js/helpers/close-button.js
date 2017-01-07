$(document).ready(function () {
    $('.close-button').on('click', function() {
        $(this).closest('.closeable').hide();
    });
});
