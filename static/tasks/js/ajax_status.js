// AJAX checkbox
$(document).ready(function() {
    $('input[type="checkbox"]').change(function() {
        let taskId = $(this).data('id');
        let status = $(this).is(':checked');

        $.ajax({
            url: '/update_status/' + taskId + '/',
            method: 'POST',
            data: {
                'status': status,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                if (response.success) {
                    console.log('Status updated successfully');
                }
            },
            error: function(xhr, status, error) {
                console.log('An error occurred:', error);
            }
        });
    });
});