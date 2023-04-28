
    const lst = document.querySelectorAll('.status-button');
    async function statusAction(el) {

        let confirmPrompt = window.confirm('Are you sure?')
        if (confirmPrompt) {
            let status = el.target.dataset['message'];
            let id = parseInt("{{queryset.id}}")
            let url = `appointment-status/${id}/${status}`
            const req = await fetch(url);
            const res =  await req.json()
            if (req.status == 200) {
                alert(JSON.stringify(res))
            }else{
                alert('Failed')
            }
        } else {
            alert('Aborted')
        }
       

    }

    for (let index = 0; index < lst.length; index++) {
        const element = lst[index];
        document.getElementById(element.id).addEventListener('click', statusAction, false)
        
    }

  