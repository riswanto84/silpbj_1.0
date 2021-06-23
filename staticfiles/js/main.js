console.log('halo dunia')
const id_kontrak = document.getElementById('id_kontrak')

function onFormSubmit(event) {
	event.preventDefault();

        var formData = new FormData();
        formData.append("file", document.getElementById("id_dokumen_pengadaan").files[0]);

        console.log(formData);

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "https://simpel.lpse.kemsos.go.id/ubah_kontrak/"+id_kontrak, true);
        xhr.upload.addEventListener("progress", function (ev){
            if(ev.lengthComputable){
                var percentage = (ev.loaded/ev.total*100|0);
                document.getElementById("progress_div").style["display"]="block";
                document.getElementById("progress_bar").style["width"]=""+percentage+"%";
                document.getElementById("progress_bar").innerHTML=""+percentage+"%";
                document.getElementById("progress_text").innerHTML="Uploaded : "+parseInt(ev.loaded/1000000)+"/"+parseInt(ev.total/1000000)+" MB";
                console.log("Uploaded : "+ev.loaded);
                console.log("TOTAL : "+ev.total);

                console.log(percentage)
            }
        });
        xhr.send(formData);

    }
