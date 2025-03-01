from audit.models import Patient, EHCPAudit, District

def admin_stats(request):
    """Context processor to add admin statistics to the context."""
    if request.path.startswith('/admin/'):
        return {
            'total_patients': Patient.objects.count(),
            'total_audits': EHCPAudit.objects.count(),
            'total_districts': District.objects.count(),
            'issues_count': Patient.objects.filter(missing_records=True).count()
        }
    return {}
