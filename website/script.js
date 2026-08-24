const API_URL =
    "https://23l3mfc7uk.execute-api.us-east-1.amazonaws.com/test/";

async function selectProduct(productId) {

    const result = document.getElementById("result");

    result.innerHTML = "Loading...";

    try {

        const response = await fetch(
            `${API_URL}/product?id=${productId}`
        );

        const product = await response.json();

        if (!response.ok) {
            throw new Error(product.error);
        }

        result.innerHTML = `
            <h2>${product.name}</h2>
            <p>Price: $${product.price}</p>
            <p>Category: ${product.category}</p>
            <p>Stock: ${product.stock}</p>
        `;

    } catch (error) {

        result.innerHTML = `
            <p>Error: ${error.message}</p>
        `;
    }
}
