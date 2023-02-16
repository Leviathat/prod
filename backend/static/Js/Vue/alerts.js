export function getAlert(type, msg) {
    let text = type === 'success' ? 'text-green-800' : type === 'info' ? 'text-blue-800' : 'text-red-800'
    let bg = type === 'success' ? 'bg-green-50' : type === 'info' ? 'bg-blue-50' : 'bg-red-50'

    let alerts = document.getElementById('alerts')
    let alert = document.createElement("div")

    alert.classList.add('alerts-list', 'flex', 'p-4', 'mb-4', text, 'rounded-lg', bg)
    alert.innerHTML = (`
  <svg aria-hidden="true" class="flex-shrink-0 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>
  <span class="sr-only">Info</span>
  <div class="ml-3 mr-2 text-sm font-medium">
    %msg
  </div>
`, msg)
    alerts.appendChild(alert)
    setTimeout(function (){
        alert.remove()
    }, 1201)
}