import { useEffect, useState } from 'react'
import Card from './Card.jsx'

export default function Products() {
    const [products, setProducts] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/products')
        .then(r => r.json())
        .then(setProducts)
        .catch(err => console.error('Error cargando productos:', err))
    }, [])

    return (
        <div>
            <h2>Productos</h2>
            {products.map((product) => (
                <div key={product.id}>
                    <h3>{product.name}</h3>
                    <p>{product.price}</p>
                </div>
            ))}
            <Card />
        </div>
    );
}