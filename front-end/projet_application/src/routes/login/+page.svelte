<script>
  import Link from "../../Components/Inputs/Link.svelte";
  let error = "";
  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const username = formData.get("username");
    const password = formData.get("password");

    console.log(username, password);

    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.token);
      location.href = "/dashboard";
    } else {
      error = await response.json();
      console.log(error);
    }
  };
</script>

<svelte:head>
  <title>Login</title>
  <meta name="description" content="Login page" />
  <link rel="stylesheet" href="src/styles/login.css" />
</svelte:head>

<section>
  <div class="login">
    <h1>Login</h1>
    <form on:submit={handleSubmit} class="login-form">
      <label for="username">Username</label>
      <input
        type="text"
        class="input-login"
        id="username"
        name="username"
        required
      />
      <label for="password">Password</label>
      <input
        type="password"
        class="input-login"
        id="password"
        name="password"
        required
      />
      {#if error}
        <p>{error}</p>
      {/if}
      <button type="submit" class="input-login">Se connecter </button>
      <Link href="register" text="Register" />
    </form>
  </div>
</section>
