import './assets/App.css';
import { BrowserRouter as Router } from "react-router-dom";
import { RoutesSwitcher } from "./project/Routes";

export default function App() {
  return (
    <div className="App">
      <Router>
        <RoutesSwitcher />
      </Router>
    </div>
  );
}
