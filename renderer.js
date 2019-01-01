const zerorpc = require("zerorpc")
let client = new zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

let formula = document.querySelector('#formula')
let result = document.querySelector('#result')
let calculate = document.querySelector('#calculate')
let photos = document.querySelector('#photos')
let uploadImage = document.querySelector('uploadImage')

calculate.addEventListener('click',() => {
  console.log(photos.value)
  client.invoke("calc", formula.value, (error, res) => {
    if(error) {
      console.error(error)
    } else {
      result.textContent = res + photos.value
      uploadImage.src = URL.createObjectURL(photos.value)
    }
  })
})
formula.dispatchEvent(new Event('input'))
