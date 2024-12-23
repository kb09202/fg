// app.js

// Exemple de données de produits
const products = [
  { id: 1, name: "Perceuse", price: 99.99, image: "https://via.placeholder.com/150" },
  { id: 2, name: "Échafaudage", price: 249.99, image: "https://via.placeholder.com/150" },
  { id: 3, name: "Coffre à outils", price: 59.99, image: "https://via.placeholder.com/150" },
  { id: 4, name: "Scie circulaire", price: 129.99, image: "https://via.placeholder.com/150" },
];

// Panier
let cart = [];

// Afficher les produits
const productList = document.getElementById("products");
products.forEach(product => {
  const productCard = document.createElement("div");
  productCard.className = "product";
  productCard.innerHTML = `
    <img src="${product.image}" alt="${product.name}">
    <h3>${product.name}</h3>
    <p>${product.price.toFixed(2)} €</p>
    <button onclick="addToCart(${product.id})">Ajouter au panier</button>
  `;
  productList.appendChild(productCard);
});

// Ajouter un produit au panier
function addToCart(productId) {
  const product = products.find(p => p.id === productId);
  const cartItem = cart.find(item => item.id === productId);

  if (cartItem) {
    cartItem.quantity++;
  } else {
    cart.push({ ...product, quantity: 1 });
  }

  updateCart();
}

// Mettre à jour le panier
function updateCart() {
  const cartList = document.getElementById("cart-items");
  cartList.innerHTML = "";

  let total = 0;

  cart.forEach(item => {
    total += item.price * item.quantity;

    const cartItem = document.createElement("li");
    cartItem.innerHTML = `
      ${item.name} x${item.quantity} - ${item.price.toFixed(2)} €
      <button onclick="removeFromCart(${item.id})">X</button>
    `;
    cartList.appendChild(cartItem);
  });

  document.getElementById("cart-total").innerText = total.toFixed(2) + " €";
}

// Retirer un produit du panier
function removeFromCart(productId) {
  cart = cart.filter(item => item.id !== productId);
  updateCart();
}
