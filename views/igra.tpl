<!DOCTYPE html>
<html>

<body>
    
    <div>
        <img src="/img/{{igra.stevilo_napak()}}.jpg" />
    </div>
    <div>
        Pravilni del gesla: {{igra.pravilni_del_gesla()}}
    </div>
    <div>
        Nepravilne črke: {{igra.nepravilni_ugibi()}}
    </div>

    <form method = "post" action = "/igra/{{id_igre}}/">
        <input name = 'crka' /> <input type ="submit" value = "Ugibaj!>
</body>

</html>