<script lang="ts">
    import type { Emploi } from "../../Models/Emploi";
    export let emploi: Emploi;

    export let handleModalClick: (id: number) => void;
</script>

<button class="offreEmploi" on:click={() => handleModalClick(emploi.id)}>
    <div class="emploi">
        <div class="info">
            <p class="text">{emploi.titre}</p>
            <p class="text">{emploi.entreprise}</p>
            <p class="text">{emploi.dateFin}</p>
            <p class="text">{emploi.description}</p>
        </div>
        <img class="image" src="add.svg" alt="ajouter" />
    </div>
</button>

<style scoped>
    .offreEmploi {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        width: 90%;
        border-width: 0px;
        border-bottom: 1px solid #00ad9a;
        margin-left: 5.2%;
        background-color: transparent;
    }
    .info {
        display: flex;
        width: 90%;
        font-size: 1.3rem;
        flex-direction: row;
        justify-content: space-around;
    }
    .text {
        width: 20%;
    }
    .emploi {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        color: white;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        width: 100%;
        height: 100%;
        padding: 5px 0px 5px 0px;
    }
    .emploi:hover {
        background-color: #555b66;
    }
    .image {
        width: 30px;
        height: 30px;
    }
</style>
