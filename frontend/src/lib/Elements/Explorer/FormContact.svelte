<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import { BsClipboard2, BsClipboard2Check } from "svelte-icons-pack/bs";
  import { URLServer } from "../../../stores/store";
  import { slide } from "svelte/transition";

  let mail = "";
  let name = "";
  let message = "";

  let mailCopied = false;
  let successVisible = false;

  let alertMail = false;
  let alertName = false;
  let alertMessage = false;

  async function copyMail() {
    await navigator.clipboard.writeText("axellajones53@gmail.com");
    mailCopied = true;
    setTimeout(() => {
      mailCopied = false;
    }, 3000);
  }

  function updateInfo (e: Event, area: string) {
    const target = e.target as HTMLInputElement;
    const value = target.value;
    if (value != null) {
        if (area === "mail") {
            mail = value;
            alertMail = false;
        } else if (area === "name") {
            name = value;
            alertName = false;
        } else if (area === "message") {
            message = value;
            alertMessage = false;
        }
    }
  }
  
  function validateForm () {
    let success = true;
    const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!name) {
        success = false;
        alertName = true;
    }
    if (!message) {
        success = false;
        alertMessage = true;
    }
    if (!regex.test(mail)) {
        success = false;
        alertMail = true;
    }

    return success
  }

  function successSend () {
    mail = "";
    name = "";
    message = "";
    successVisible = true;
    setTimeout(() => {
        successVisible = false;
    }, 3000)
  }

  async function sendMessage () {
    if (!validateForm()) {
        return
    }
    const res = await fetch(`${$URLServer}/api/send_mail`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({name: name, mail: mail, message: message})
    })
    if (res.ok) {
        successSend()
    }
  }

</script>

<div class="flex flex-col place-items-center">
  <button
    class="flex flex-row gap-1 w-fit text-neutral-400 rounded-full py-1 px-2 hover:text-neutral-200"
    on:click={copyMail}
  >
    <Icon src={mailCopied ? BsClipboard2Check : BsClipboard2} size={22} />
    <span class="font-extralight">Copiar correo</span>
  </button>
  <div class=" text-neutral-300">
    <div class="flex flex-col gap-2 place-items-center">
      <div class="flex flex-col">
        <label for="mail">Correo</label>
        <input
          type="text"
          name="mail"
          placeholder="Ingrese su correo"
          required
          class=" bg-transparent border rounded px-1 text-neutral-400 w-40 {alertMail ? 'border-red-500' : ''}"
        on:input={e=>updateInfo(e, "mail")} value={mail}/>
      </div>
      <div class="flex flex-col">
        <label for="name">Nombre</label>
        <input
          type="text"
          name="name"
          placeholder="Ingrese su nombre"
          required
          class=" bg-transparent border rounded px-1 text-neutral-400 w-40 {alertName ? 'border-red-500' : ''}"
        on:input={e=>updateInfo(e, "name")} value={name}/>
      </div>
      <div class="flex flex-col">
        <label for="message">Mensaje</label>
        <textarea
          name="message"
          required
          class="bg-transparent border rounded px-1 text-neutral-400 w-40 outline-none {alertMessage ? 'border-red-500' : ''}"
        on:input={e=>updateInfo(e, "message")} value={message}></textarea>
      </div>
      <button
        class="border rounded px-2 w-fit place-self-center hover:bg-neutral-800 hover:cursor-pointer"
      on:click={sendMessage}>
        Enviar
      </button>
      {#if successVisible}
        <p transition:slide class="bg-lime-400 text-neutral-900 w-full text-center font-semibold">Mensaje recibido</p>
      {/if}
    </div>
  </div>
</div>
