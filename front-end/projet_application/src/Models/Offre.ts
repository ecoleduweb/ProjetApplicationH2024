

export interface Offre { 
    titre: string; // titre de l'offre
    lieu: string; // lieu de travail
    active: boolean; // si l'offre est active ou non
    dateEntreeFontion: Date // date d'entrée en fonction
    dateLimitePostuler: Date // date limite pour postuler

    heure: string; // heure par semaine
    salaire: string; // salaire de lheure 
    stage: boolean; // si stage vrai sinon faux
    duree: string; // temps partiel, temps plein
    programme: string; // le programme visée par l'offre
    conciliation: boolean; // employeur conciliant ou non
    urgente: boolean; // si l'offre est urgente
    lien: string; // lien vers l'offre ou site web de l'employeur
    description: string; // description de l'offre
    dateAffichageDebut: string; // date de début de l'affichage
    dateAffichageFin: string; // date de fin de l'affichage
    personneContact: string; // nom de la personne à contacter
    courrielContact: string; // courriel de la personne à contacter
    telephoneContact: string; // téléphone de la personne à contacter
} 