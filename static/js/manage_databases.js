    function getDatabases() {
      $.get('/api/databases/').then(
          function (res) {
              console.log(res);
          }
      )
    }
    function testDatabase(){
        $.post('/api/databases/testdb/',$('#databaseform').serialize()).then(
            function (res) {
                console.log(res, typeof(res),$('.btn btn-primary disabled'));
                if(res){
                    $('.btn btn-primary disabled').removeClass('disabled');
                }
            }
        )
    }

    function addDatabase(){

    }

    document.addEventListener('DOMContentLoaded',function () {
        getDatabases();
    });
