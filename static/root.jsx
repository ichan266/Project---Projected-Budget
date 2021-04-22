// import github from "static/GitHub-Mark-Light-64px.png";

const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useParams = ReactRouterDOM.useParams;
const useHistory = ReactRouterDOM.useHistory;

function Homepage() {
  return <div> Welcome to my site </div>;
}

// function AboutMe() {
//   return <a href="/templates/aboutme.html">About Me</a>;
// }

function ConnectWithMe() {
  return (
    <img
      className="logo"
      src={require("static/GitHub-Mark-Light-64px.png")}
      alt="GitHub logo"
    />
  );
}

function SearchBar() {
  return (
    <div>
      <input type="text"></input>
    </div>
  );
}

function Search() {
  return (
    <div>
      Search for some stuff
      <SearchBar />
    </div>
  );
}
// * Here, we call the SearchBar component. So we can break things up when it gets too big

function LogIn() {
  console.log(email);
  // Login for users
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  // Registration for new users
  const [firstName, setFirstName] = React.useState("");
  const [lastName, setLastName] = React.useState("");
  const [newEmail, setNewEmail] = React.useState("");
  const [newPassword, setNewPassword] = React.useState("");

  function handleLogin(evt) {
    evt.preventDefault();
    const data = {
      email: email,
      password: password,
    };
    // console.log(email)
    // console.log(password)
    // alert("you submitted the form");

    const options = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    fetch("/api/login", options)
      .then((response) => response.json())
      .then((data) => {
        if (data) {
          alert(data);
        } else {
          alert("no muffins, very sad");
        }
      });
  }
  // * JSON.stringify turns JavaScript objects (i.e. data) into a string
  // * .then is a method used with a promise. Once we capture the information as `response` from the server, we call a function. Once we received it, we want to "hydrate" it (i.e. turning it back to JavaScript Object)

  function handleEmailChange(evt) {
    let what_they_just_typed = evt.target.value;
    console.log(what_they_just_typed);
    setEmail(evt.target.value);
  }

  function handlePasswordChange(evt) {
    let what_they_just_typed = evt.target.value;
    console.log(what_they_just_typed);
    setPassword(evt.target.value);
  }

  function handleNewUser(evt) {
    evt.preventDefault();
    const newData = {
      firstName: firstName,
      lastName: lastName,
      newEmail: newEmail,
      newPassword: newPassword,
      newPasswordConf: newPasswordConf,
    };

    const newOptions = {
      method: "POST",
      body: JSON.stringify(newData),
      headers: {
        "Content-Type": "application/json",
      },
    };
    fetch("/api/");
  }

  return (
    <div>
      <form className="form" onSubmit={handleLogin}>
        <h3>Please Sign In</h3>
        <label htmlFor="sign_in_email" className="sr-only">
          Email address
        </label>
        <input
          value={email}
          onChange={handleEmailChange}
          type="email"
          id="sign_in_email"
          className="form-control"
          name="email"
          placeholder="Email address"
          required
          autoFocus
        />
        <label htmlFor="inputPassword" className="sr-only">
          Password
        </label>
        <input
          value={password}
          onChange={handlePasswordChange}
          type="password"
          id="inputPassword"
          className="form-control"
          name="password"
          placeholder="Password"
          required
        />
        <button className="btn btn-lg btn-success btn-block">Sign In</button>
      </form>

      <form className="form" id="create_user" onSubmit={handleNewUser}>
        <h3>Sign Up Here</h3>
        <label htmlFor="inputFirstName" className="sr-only">
          First Name
        </label>
        <input
          value={firstName}
          type="text"
          id="inputFirstName"
          className="form-control"
          name="first_name"
          placeholder="First Name"
          required
        />
        <label htmlFor="inputLastName" className="sr-only">
          Last Name
        </label>
        <input
          value={lastName}
          type="text"
          id="inputLastName"
          className="form-control"
          name="last_name"
          placeholder="Last Name"
          required
        />
        <label htmlFor="inputNewEmail" className="sr-only">
          Email address
        </label>
        <input
          value={newEmail}
          type="email"
          id="inputEmail"
          className="form-control"
          name="new_email"
          placeholder="Email"
          required
        />
        <label htmlFor="newPassword" className="sr-only">
          Password
        </label>
        <input
          value={newPassword}
          type="password"
          id="inputPassword"
          className="form-control"
          name="newPassword"
          placeholder="Password"
          required
        />
        <input
          value={newPasswordConf}
          type="password"
          id="new_password_conf"
          className="form-control"
          name="newPasswordConf"
          placeholder="Please Confirm Password"
          required
        />
        <button className="btn btn-lg btn-primary btn-block">Sign Up</button>
      </form>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div>
        <LogIn />

        {/* <Switch>
          <Route path="/login">
            <LogIn />
          </Route>

          <Route path="/connectwithme">
            <ConnectWithMe />
          </Route>

          <Route path="/search">
            <Search />
          </Route>

          <Route path="/">
            <Homepage />
          </Route>
        </Switch> */}
      </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));

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
