import React, { useEffect, useState } from "react";
import '../static/Main.css';
import { Button, Container, Form, Nav, Navbar } from "react-bootstrap";
import Apis, { endpoints } from "../configs/Apis";
import Logo from '../images/logo.png'


const Header = () => {
    const [categories, setCategories] = useState([])

    useEffect(() => {
        const loadCategories = async () => {
            const res = await Apis.get(endpoints['categories'])
            setCategories(res.data)
        }
        loadCategories()
    }, [])

    return (
        <Navbar expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="dark">
            <Container>
                <Navbar.Brand>
                    <img className="logo" src={Logo} alt="Cellmobile Logo" />
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="me-auto my-2 my-lg-0"
                        style={{ maxHeight: '100px' }}
                        navbarScroll
                    >
                        {categories.map(c => {
                            return <Nav.Link key={c.id} href="#">{c.name}</Nav.Link>
                        })}
                    </Nav>
                    <Form className="d-flex">
                        <Form.Control
                            type="search"
                            placeholder="Search"
                            className="me-2"
                            aria-label="Search"
                        />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default Header