import React, { useEffect, useState } from "react";
import "../static/Main.css";
import { Carousel, Container, Row } from "react-bootstrap";
import Apis, { endpoints } from "../configs/Apis";
import HomeProduct from "../components/HomeProduct";


const Home = () => {
    const [banners, setBanners] = useState([])
    const [products, setProducts] = useState([])

    useEffect(() => {
        const loadBanners = async () => {
            const res = await Apis.get(endpoints['banners'])
            setBanners(res.data)
        }
        loadBanners()
    }, [])

    useEffect(() => {
        const loadProducts = async () => {
            const res = await Apis.get(endpoints['products'])
            setProducts(res.data.results)
        }
        loadProducts()
    }, [])

    return (
        <>
            <Carousel fade>
                {banners.map(b =>
                    <Carousel.Item key={b.id}>
                        <img className="d-block w-100" src={b.image} alt={b.name} />
                    </Carousel.Item>
                )}
            </Carousel>
            <Container style={{ marginTop: "20px" }}>
                <div className="column large-8 small-12 rs-shop-header-section">
                    <h1 className="rs-shop-header">Cửa Hàng.</h1>
                    <div className="rs-shop-subheader">Cách tốt nhất để mua sản phẩm bạn thích.</div>
                </div>
                <Row className="owl-stage">
                    {products.map(p => {
                        return <HomeProduct key={p.id} name={p.name} image={p.image} price={p.price} />
                    })}
                </Row>
            </Container>
        </>
    )
}

export default Home