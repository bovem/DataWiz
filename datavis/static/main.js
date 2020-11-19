$(document).ready(function () {
    $.noConflict();
    $('.table').DataTable();
    $(document).scrollTop($(document).height());

});

function addCleaner() {
    console.log('reached till cleaner')
    fetch('/', {
        method: 'POST',
        body: JSON.stringify({
            cell: 'cleaner.html',
            data: {
                // Adding other params of the block 
            }
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json();
    }).then((data) => {
        if (data['data'] == 'success') {
            console.log(data)
            window.location.href = '/'
        }
    })
}
