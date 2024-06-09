// src/Navbar.js 
// Author: Louis Chang
// DESCRIPTION: This file contains the implementation of the navigation bar component.
// Version 0.2 - 2024/06/09

// - Version 0.1 - 2024/06/02: Create the Navbar component.
// - Version 0.2 - 2024/06/09: Add links for Chat and Settings pages.

import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <Link className="navbar-brand" to="/">Cockatoo.AI</Link>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link className="nav-link" to="/">Home</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" to="/settings">Settings</Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
