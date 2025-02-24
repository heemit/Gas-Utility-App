from django.contrib.auth.models     import AbstractUser, Group, Permission
from django.db                      import models
from django.core.validators         import FileExtensionValidator

# Custom User Model
class User(AbstractUser):
    phone   = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups  = models.ManyToManyField(
        Group,
        related_name="web_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="web_user_permissions_set",
        blank=True
    )

    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Service Request Model
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    user            = models.ForeignKey(User, on_delete=models.CASCADE)  # Use the custom User model
    request_type    = models.CharField(max_length=255)
    description     = models.TextField()
    attachment      = models.FileField(
        upload_to   ='attachments/',
        validators  =[FileExtensionValidator(['jpg', 'png', 'pdf'])],
        blank=True, null=True
    )
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Automatically incremented ID per user
    service_id      = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'service_id'], name='unique_service_id_per_user')
        ]

    def save(self, *args, **kwargs):
        if self.service_id is None:
            # Get the next service ID for this user
            max_service_id  = ServiceRequest.objects.filter(user=self.user).aggregate(models.Max('service_id'))['service_id__max']
            self.service_id = max_service_id + 1 if max_service_id is not None else 1
        super(ServiceRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"Service ID {self.service_id} - {self.request_type} - {self.status}"