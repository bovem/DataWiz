Dropzone.autoDiscover = false;
$(document).ready(function () {
    $.noConflict();
    a = $('.table').DataTable();
    

    var currCell = $('div.currentCell').get(0)
    if(currCell !== undefined)
        currCell.scrollIntoView()

    var dropzone = new Dropzone('#dropzone');
    // console.log(dropzone)
    dropzone.on('success', function(file, resp) {
        console.log('a')
        window.location.href = '/'
    })
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
