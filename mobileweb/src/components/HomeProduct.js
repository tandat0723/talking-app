import React, { memo } from "react";
import { Card, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import '../static/Main.css'

const HomeProduct = (props) => {
    let path = `/products/${props.id}/`
    return (
        <Col className="item" md={3} xs={12}>
            <Link className="custom-card" to={path} style={{ textDecoration: "none" }}>
                <Card style={{border: "none"}}>
                    <Card.Body>
                        <Card.Title>{props.name}</Card.Title>
                    </Card.Body>
                    <Card.Img className="img-slide" variant="top" src={props.image} />
                    <Card.Body>
                        <Card.Title>{props.price} VNĐ</Card.Title>
                    </Card.Body>
                </Card>
            </Link>
        </Col>
    )
}
export default memo(HomeProduct)