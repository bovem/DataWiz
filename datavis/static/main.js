Dropzone.autoDiscover = false;
$(document).ready(function () {
    $("#formatted-table").on('change',function() {
        if(!this.checked) {
            $('.table-div').hide();
            $('.array-div').show();
        }
        else {
            $('.table-div').show();
            $('.array-div').hide();
        }
    })
    $.noConflict();
    // a = $('.table').DataTable();

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

function confirmReset(){
    var a = confirm('Are you sure want to reset the workspace?')
    if(a == true) {
        fetch('/reset')
        window.location.href = '/'
    }
}

