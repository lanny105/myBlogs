KindEditor.ready(function(K) {
    K.create('textarea[name=content]',{
        height:"300",
        width:"1024",
        uploadJson:'/admin/upload/kindeditor',
    });
});