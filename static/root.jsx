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

function About() {
  return <div> A tiny react demo site </div>
}


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
              <Link to="/about"> About </Link> 
            </li>
            <li>
              <Link to="/search"> Search </Link> 
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/about">
            <About />
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
// $ What pages do I want to have for the users, ie. what is my main components
// $ There are stuff you want to render in every page (just like base.html), such as nav bar
// ! Make sure after you write the link, you also need to put Route and call the component