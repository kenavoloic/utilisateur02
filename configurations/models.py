from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import Group, User
from django.urls import reverse

class Societe(models.Model):
    nom = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Société"
        verbose_name_plural = "Sociétés"
        ordering = ['id'] # 'created_at' ou 'nom'

class Service(models.Model):
    nom = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['id']

class Site(models.Model):
    nom = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{5}$', 'Un code postal français contient au moins 5 caractères')])
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.nom} ({self.code_postal})"

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ['id','code_postal']

class Conducteur(models.Model):
    erp_id = models.IntegerField(unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField(null=True, blank=True)
    date_entree = models.DateField()
    date_sortie = models.DateField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    actif_p = models.BooleanField(default=True, verbose_name="Actif")
    interim_p = models.BooleanField(default=False, verbose_name="Intérim")

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Conducteur"
        verbose_name_plural = "Conducteurs"
        ordering = ['nom', 'prenom']        

# class Notateur(models.Model):
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     date_entree = models.DateField()
#     date_sortie = models.DateField(null=True, blank=True)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.prenom} {self.nom}"

#     @property
#     def nom_complet(self):
#         return f"{self.prenom} {self.nom}"

#     class Meta:
#         verbose_name = "Notateur"
#         verbose_name_plural = "Notateurs"

class CriteresNotation(models.Model):
    nom = models.CharField(max_length=255)
    valeur_mini = models.IntegerField()
    valeur_maxi = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.nom} {self.valeur_mini}-{self.valeur_maxi}"

    class Meta:
        verbose_name = "Critère de notation"
        verbose_name_plural = "Critères de notation"
        ordering = ['id', 'nom']

# class Notation(models.Model):
#     date_notation = models.DateField()
#     notateur = models.ForeignKey(Notateur, on_delete=models.CASCADE)
#     conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
#     critere = models.ForeignKey(CriteresNotation, on_delete=models.CASCADE)
#     valeur = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.conducteur} - {self.critere} : {self.valeur}"

#     class Meta:
#         verbose_name = "Notation"
#         verbose_name_plural = "Notations"
#         unique_together = ['conducteur', 'critere', 'date_notation', 'notateur']

# class HistoriqueNotation(models.Model):
#     notation = models.ForeignKey(Notation, on_delete=models.CASCADE)
#     critere = models.ForeignKey(CriteresNotation, on_delete=models.CASCADE)
#     ancienne_valeur = models.IntegerField(null=True, blank=True)
#     nouvelle_valeur = models.IntegerField()
#     date_changement = models.DateTimeField(default=timezone.now)

#     class Meta:
#         verbose_name = "Historique de notation"
#         verbose_name_plural = "Historiques de notation"

# class HistoriqueSite(models.Model):
#     conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
#     site = models.ForeignKey(Site, on_delete=models.CASCADE)
#     date_entree = models.DateField()
#     date_sortie = models.DateField(null=True, blank=True)

#     class Meta:
#         verbose_name = "Historique de site"
#         verbose_name_plural = "Historiques de site"        


class GroupePage(models.Model):
    """Modèle pour définir les groupes de pages"""
    nom = models.CharField(max_length=50, unique=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ordre = models.IntegerField(default=0, help_text="Ordre d'affichage dans la navbar")
    
    class Meta:
        ordering = ['ordre', 'nom']
    
    def __str__(self):
        return self.libelle

class Page(models.Model):
    """Modèle pour définir les pages et leurs associations aux groupes"""
    nom = models.CharField(max_length=50, unique=True)
    libelle = models.CharField(max_length=255)
    nom_url = models.CharField(max_length=100, help_text="Nom de l'URL Django")
    groupe = models.ForeignKey(GroupePage, on_delete=models.CASCADE, related_name='pages_list')
    ordre = models.IntegerField(default=0, help_text="Ordre dans le groupe")
    is_active = models.BooleanField(default=True)
    #icon_class = models.CharField(max_length=50, blank=True, help_text="Classe CSS pour l'icône")
    
    class Meta:
        ordering = ['groupe', 'ordre', 'nom']
    
    def __str__(self):
        return f"{self.libelle} ({self.groupe.nom})"
    
    def get_url(self):
        """Retourne l'URL de la page"""
        try:
            return reverse(self.nom_url)
        except:
            return "#"

class PageConfig(models.Model):
    """Configuration des pages - PAS le contenu (qui reste dans les templates)"""
    # name = models.CharField(max_length=100, unique=True)  # Identifiant technique
    # display_name = models.CharField(max_length=200)       # Nom affiché dans la navbar
    # group = models.ForeignKey(GroupePage, on_delete=models.CASCADE, related_name='pages')

    nom = models.CharField(max_length=100, unique=True)  # Identifiant technique
    libelle = models.CharField(max_length=200)       # Nom affiché dans la navbar
    groupe = models.ForeignKey(GroupePage, on_delete=models.CASCADE, related_name='pages_config')
    
    # Routing
    url_pattern = models.CharField(max_length=200)  # 'dashboard/', 'reports/sales/'
    nom_template = models.CharField(max_length=200)  # 'pages/admin/dashboard.html'
    
    # Navigation
    ordre = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)  # Page par défaut du groupe
    show_in_navbar = models.BooleanField(default=True)
    
    # Métadonnées (pour le <head> HTML)
    titre_page = models.CharField(max_length=200, blank=True)
    #meta_description = models.CharField(max_length=300, blank=True)
    
    # Permissions étendues (optionnel)
    #require_ssl = models.BooleanField(default=False)
    #cache_timeout = models.IntegerField(default=300)  # 5 minutes par défaut
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['groupe', 'ordre', 'nom']
        unique_together = [['groupe', 'ordre']]
    
    def __str__(self):
        return f"{self.groupe.nom} - {self.libelle}"
    
    def get_titre_complet(self):
        """Titre complet pour le <title>"""
        if self.titre_page:
            return f"{self.titre_page} | Mon App"
        return f"{self.libelle} | Mon App"
    
class AssociationUtilisateurGroupe(models.Model):
    """Association entre utilisateurs et groupes de pages"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page_group = models.ForeignKey(GroupePage, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['user', 'page_group']
    
    def __str__(self):
        return f"{self.user.username} - {self.page_group.nom}"
