

// $('#btnlogin').click(function (e) {
//     alert(hello);
//     e.preventDefault();
//     frm = $('#signinform');
//     btn = $('this');
//     btn.html("<i class='fa fa-cog fa-spin'></i>processing");
//
//     $.ajax({
//         url: '/signin',
//         method: 'POST',
//         data: frm.serialize(),
//        success: function (data) {
//             if(data !== 'ok'){
//                 alert('hello')
//                 btn.html('login')
//             }
//        }
//
//     })
//
// })

$('#signinform').submit(function (e) {
    e.preventDefault();
    frm = $('#signinform');
    btn = $('#btnlogin');
    btn.html("<i class='fa fa-cog fa-spin'></i> Processing...");
    $.ajax({
        url: '/signin',
        method: 'POST',
        data: frm.serialize(),
        success: function (data) {
            if (data != 'ok') {
                Swal.fire({
                    title: 'Error!',
                    text: data,
                    icon: 'error',
                    confirmButtonText: 'Try Again'
                });
                btn.html('Log In');
            } else {
                Swal.fire({
                    title: 'Bravo!',
                    text: data,
                    icon: 'success',
                    confirmButtonText: 'Ok!'
                });
                setTimeout(()=> {
                    document.location.assign('/dashboard');
                }, 3000)
            }

        }
    });
});