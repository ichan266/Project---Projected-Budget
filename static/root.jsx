const Router = ReactRouterDOM.BrowserRouter;
const Route =  ReactRouterDOM.Route;
const Link =  ReactRouterDOM.Link;
const Prompt =  ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useParams = ReactRouterDOM.useParams;
const useHistory = ReactRouterDOM.useHistory;

function Homepage() {
  return <div> Welcome to my site </div>
}

function AboutMe() {
  return <a href="/templates/aboutme.html">About Me</a>
}

// function ConnectWithMe() {
//   return (
//     <>
//       <a href="https://github.com/ichan266/Project---Projected-Budget">
//         <img class="logo" src="/static/GitHub-Mark-Light-64px.png"></a>
//       <a href="https://www.linkedin.com/in/iris-kuhn/">
//         <img class="logo" src="/static/LI-In-Bug.png"></a>
//       <a href="https://twitter.com/ichan266">
//         <img class="logo" src="/static/Twitter-icon.png"></a>
//       <a href="https://youtu.be/G3zVo_hxHpk">
//         <img class="logo" src="/static/youtube_logo.png"></a>
//     <>
//   )
// }

function SearchBar() {
  return (
    <div>
      <input type="text"></input>
    </div>
  )
}

function Search() {
  return (
    <div> 
      Search for some stuff
      <SearchBar />
    </div>
  )
}
// * Here, we call the SearchBar component. So we can break things up when it gets too big

function LogIn() {

  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')

  function handleLogin(evt) {
    evt.preventDefault();
    const data = {
      email: email,
      password: password
    }
    // console.log(email)
    // console.log(password)
    // alert('you submitted the form')

    const options = {
      method: 'POST',
      body: JSON.stringify(data),  
      headers: {  
        'Content-Type': 'application/json'
      },
    } 
    fetch('/api/login', options) 
    .then(response => response.json())
    .then(data => {
      if (data) {
        alert(data)
      } else {
        alert('no muffins, very sad')
      }
    })
  }
  // * JSON.stringify turns JavaScript objects (i.e. data) into a string
  // * .then is a method used with a promise. Once we capture the information as `response` from the server, we call a function. Once we received it, we want to "hydrate" it (i.e. turning it back to JavaScript Object)

  function handleEmailChange(evt) {
    let what_they_just_typed = evt.target.value
    console.log(what_they_just_typed)
    setEmail(evt.target.value)
  }

  function handlePasswordChange(evt) {
    let what_they_just_typed = evt.target.value
    console.log(what_they_just_typed)
    setPassword(evt.target.value)
  }

  return (
    <div>
      <form onSubmit={handleLogin}>
        Username:
        <input value={email} onChange={handleEmailChange} type="text"></input>
        Password:
        <input value={password} onChange={handlePasswordChange} type="text"></input>
        <button>Login</button>
      </form>
    </div>
  )
}

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/"> Home </Link>
            </li>
            <li>
              <Link to="/aboutme"> About Me</Link> 
            </li>
            <li>
              <Link to="/search"> Search </Link> 
            </li>
            <li>
              <LogIn />
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/login">
            <LogIn />
          </Route>
          
          <Route path="/aboutme">
            <AboutMe />
          </Route>

          <Route path="/search">
            <Search />
          </Route>
          
          <Route path="/">
            <Homepage />
          </Route>
        </Switch>

      </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

//* `Link` only changes in the URL but there was not HTTP request sent to the server

// $ 3/14/21
// @ What pages do I want to have for the users, ie. what is my main components
// @ There are stuff you want to render in every page (just like base.html), such as nav bar
// ! Make sure after you write the link, you also need to put Route and call the component

// $ 3/15/21
// @ Start off with building one component for each view for my site
// @ We will now pass information with JSON
// @ ~ Make sure to check out the mdn doc for fetch! Fetch in vanilla JS
// @ https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
// @ options = {method: "POST"}
// @ fetch('/api/login', options) makes a POST request to that URL. Without the 2nd argument, it will be a GET request

// $ 3/21/21
// ! HTTP ONLY SUPPORT STRING!!!!!
// @ JavaScript objects are not string, but JSON is! So we can send everything back and forth as JSON