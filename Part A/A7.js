const num = document.querySelector('#number')
const result = document.querySelector('.result')
document.querySelector('.submit').addEventListener('click', e =>{
    e.preventDefault()
    if(num.value)
    {
        if(num.value == 0)
            result.innerHTML = "False"
        else if(num.value%3==0 || num.value%7==0)
            result.innerHTML = "True"
        else
            result.innerHTML = "False"
    }
    else
        result.innerHTML = ""
})