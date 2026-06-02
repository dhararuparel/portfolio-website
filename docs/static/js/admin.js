// Admin Dashboard JavaScript with full CRUD functionality

class AdminAPI {
    constructor() {
        this.baseURL = '/api';
    }

    async request(url, options = {}) {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    // Projects API
    async getProjects() {
        return await this.request(`${this.baseURL}/projects`);
    }

    async getProject(id) {
        return await this.request(`${this.baseURL}/projects/${id}`);
    }

    async createProject(data) {
        return await this.request(`${this.baseURL}/projects`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateProject(id, data) {
        return await this.request(`${this.baseURL}/projects/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteProject(id) {
        return await this.request(`${this.baseURL}/projects/${id}`, {
            method: 'DELETE'
        });
    }

    // Skills API
    async getSkills() {
        return await this.request(`${this.baseURL}/skills`);
    }

    async getSkill(id) {
        return await this.request(`${this.baseURL}/skills/${id}`);
    }

    async createSkill(data) {
        return await this.request(`${this.baseURL}/skills`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateSkill(id, data) {
        return await this.request(`${this.baseURL}/skills/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteSkill(id) {
        return await this.request(`${this.baseURL}/skills/${id}`, {
            method: 'DELETE'
        });
    }

    // Education API
    async getEducation() {
        return await this.request(`${this.baseURL}/education`);
    }

    async getEducationItem(id) {
        return await this.request(`${this.baseURL}/education/${id}`);
    }

    async createEducation(data) {
        return await this.request(`${this.baseURL}/education`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateEducation(id, data) {
        return await this.request(`${this.baseURL}/education/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteEducation(id) {
        return await this.request(`${this.baseURL}/education/${id}`, {
            method: 'DELETE'
        });
    }

    // Certifications API
    async getCertifications() {
        return await this.request(`${this.baseURL}/certifications`);
    }

    async getCertification(id) {
        return await this.request(`${this.baseURL}/certifications/${id}`);
    }

    async createCertification(data) {
        return await this.request(`${this.baseURL}/certifications`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateCertification(id, data) {
        return await this.request(`${this.baseURL}/certifications/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteCertification(id) {
        return await this.request(`${this.baseURL}/certifications/${id}`, {
            method: 'DELETE'
        });
    }

    // Internships API
    async getInternships() {
        return await this.request(`${this.baseURL}/internships`);
    }

    async getInternship(id) {
        return await this.request(`${this.baseURL}/internships/${id}`);
    }

    async createInternship(data) {
        return await this.request(`${this.baseURL}/internships`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateInternship(id, data) {
        return await this.request(`${this.baseURL}/internships/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteInternship(id) {
        return await this.request(`${this.baseURL}/internships/${id}`, {
            method: 'DELETE'
        });
    }

    // Contact API
    async getContact() {
        return await this.request(`${this.baseURL}/contact`);
    }

    async createContact(data) {
        return await this.request(`${this.baseURL}/contact`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updateContact(data) {
        return await this.request(`${this.baseURL}/contact`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }
}

// Initialize API
const api = new AdminAPI();

// Utility functions
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    document.querySelectorAll('.admin-toast').forEach(n => n.remove());
    notification.className = `admin-toast ${type === 'error' ? 'error' : 'success'}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 5000);
}

function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
    const form = document.querySelector(`#${modalId} form`);
    if (form) {
        form.reset();
        const idField = form.querySelector('input[type="hidden"]');
        if (idField) idField.value = '';
    }
}

// Project functions
async function editProject(id) {
    try {
        const project = await api.getProject(id);
        
        document.getElementById('projectId').value = project.id;
        document.getElementById('projectTitle').value = project.title;
        document.getElementById('projectDescription').value = project.description;
        document.getElementById('projectTechnologies').value = project.technologies;
        document.getElementById('projectDuration').value = project.duration;
        document.getElementById('projectTeamSize').value = project.team_size;
        document.getElementById('projectRole').value = project.role;
        document.getElementById('projectLinkUrl').value = project.link_url || '';
        document.getElementById('projectLinkLabel').value = project.link_label || '';
        
        document.getElementById('projectModalTitle').textContent = 'Edit Project';
        openModal('projectModal');
    } catch (error) {
        showNotification('Error loading project: ' + error.message, 'error');
    }
}

async function deleteProject(id) {
    if (!confirm('Are you sure you want to delete this project?')) return;
    
    try {
        await api.deleteProject(id);
        showNotification('Project deleted successfully');
        location.reload(); // Refresh to update the table
    } catch (error) {
        showNotification('Error deleting project: ' + error.message, 'error');
    }
}

// Skill functions
async function editSkill(id) {
    try {
        const skill = await api.getSkill(id);
        
        document.getElementById('skillId').value = skill.id;
        document.getElementById('skillName').value = skill.name;
        document.getElementById('skillCategory').value = skill.category;
        
        document.getElementById('skillModalTitle').textContent = 'Edit Skill';
        openModal('skillModal');
    } catch (error) {
        showNotification('Error loading skill: ' + error.message, 'error');
    }
}

async function deleteSkill(id) {
    if (!confirm('Are you sure you want to delete this skill?')) return;
    
    try {
        await api.deleteSkill(id);
        showNotification('Skill deleted successfully');
        location.reload();
    } catch (error) {
        showNotification('Error deleting skill: ' + error.message, 'error');
    }
}

// Education functions
async function editEducation(id) {
    try {
        const education = await api.getEducationItem(id);
        
        document.getElementById('educationId').value = education.id;
        document.getElementById('educationDegree').value = education.degree;
        document.getElementById('educationInstitution').value = education.institution;
        document.getElementById('educationYear').value = education.year;
        document.getElementById('educationPercentage').value = education.percentage || '';
        
        document.getElementById('educationModalTitle').textContent = 'Edit Education';
        openModal('educationModal');
    } catch (error) {
        showNotification('Error loading education: ' + error.message, 'error');
    }
}

async function deleteEducation(id) {
    if (!confirm('Are you sure you want to delete this education entry?')) return;
    
    try {
        await api.deleteEducation(id);
        showNotification('Education deleted successfully');
        location.reload();
    } catch (error) {
        showNotification('Error deleting education: ' + error.message, 'error');
    }
}

// Certification functions
async function editCertification(id) {
    try {
        const certification = await api.getCertification(id);
        
        document.getElementById('certificationId').value = certification.id;
        document.getElementById('certificationTitle').value = certification.title;
        document.getElementById('certificationIssuer').value = certification.issuer;
        document.getElementById('certificationPercentage').value = certification.percentage || '';
        document.getElementById('certificationDateRange').value = certification.date_range || '';
        
        document.getElementById('certificationModalTitle').textContent = 'Edit Certification';
        openModal('certificationModal');
    } catch (error) {
        showNotification('Error loading certification: ' + error.message, 'error');
    }
}

async function deleteCertification(id) {
    if (!confirm('Are you sure you want to delete this certification?')) return;
    
    try {
        await api.deleteCertification(id);
        showNotification('Certification deleted successfully');
        location.reload();
    } catch (error) {
        showNotification('Error deleting certification: ' + error.message, 'error');
    }
}

// Internship functions
async function editInternship(id) {
    try {
        const internship = await api.getInternship(id);
        
        document.getElementById('internshipId').value = internship.id;
        document.getElementById('internshipPosition').value = internship.position;
        document.getElementById('internshipCompany').value = internship.company;
        document.getElementById('internshipDuration').value = internship.duration;
        document.getElementById('internshipLocation').value = internship.location;
        document.getElementById('internshipTechnologies').value = internship.technologies || '';
        document.getElementById('internshipDescription').value = internship.description || '';
        
        document.getElementById('internshipModalTitle').textContent = 'Edit Internship';
        openModal('internshipModal');
    } catch (error) {
        showNotification('Error loading internship: ' + error.message, 'error');
    }
}

async function deleteInternship(id) {
    if (!confirm('Are you sure you want to delete this internship?')) return;
    
    try {
        await api.deleteInternship(id);
        showNotification('Internship deleted successfully');
        location.reload();
    } catch (error) {
        showNotification('Error deleting internship: ' + error.message, 'error');
    }
}

// Contact functions
async function editContact(id) {
    try {
        const contact = await api.getContact();
        
        document.getElementById('contactId').value = contact.id;
        document.getElementById('contactPhone').value = contact.phone;
        document.getElementById('contactEmail').value = contact.email;
        document.getElementById('contactLocation').value = contact.location;
        document.getElementById('contactLinkedin').value = contact.linkedin || '';
        
        document.getElementById('contactModalTitle').textContent = 'Edit Contact Info';
        openModal('contactModal');
    } catch (error) {
        showNotification('Error loading contact: ' + error.message, 'error');
    }
}

// Form submission handlers
document.addEventListener('DOMContentLoaded', function() {
    // Project form
    const projectForm = document.getElementById('projectForm');
    if (projectForm) {
        projectForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateProject(id, data);
                    showNotification('Project updated successfully');
                } else {
                    await api.createProject(data);
                    showNotification('Project created successfully');
                }
                closeModal('projectModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving project: ' + error.message, 'error');
            }
        });
    }

    // Skill form
    const skillForm = document.getElementById('skillForm');
    if (skillForm) {
        skillForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateSkill(id, data);
                    showNotification('Skill updated successfully');
                } else {
                    await api.createSkill(data);
                    showNotification('Skill created successfully');
                }
                closeModal('skillModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving skill: ' + error.message, 'error');
            }
        });
    }

    // Education form
    const educationForm = document.getElementById('educationForm');
    if (educationForm) {
        educationForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateEducation(id, data);
                    showNotification('Education updated successfully');
                } else {
                    await api.createEducation(data);
                    showNotification('Education created successfully');
                }
                closeModal('educationModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving education: ' + error.message, 'error');
            }
        });
    }

    // Certification form
    const certificationForm = document.getElementById('certificationForm');
    if (certificationForm) {
        certificationForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateCertification(id, data);
                    showNotification('Certification updated successfully');
                } else {
                    await api.createCertification(data);
                    showNotification('Certification created successfully');
                }
                closeModal('certificationModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving certification: ' + error.message, 'error');
            }
        });
    }

    // Internship form
    const internshipForm = document.getElementById('internshipForm');
    if (internshipForm) {
        internshipForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateInternship(id, data);
                    showNotification('Internship updated successfully');
                } else {
                    await api.createInternship(data);
                    showNotification('Internship created successfully');
                }
                closeModal('internshipModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving internship: ' + error.message, 'error');
            }
        });
    }

    // Contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            const id = data.id;
            delete data.id;
            
            try {
                if (id) {
                    await api.updateContact(data);
                    showNotification('Contact info updated successfully');
                } else {
                    await api.createContact(data);
                    showNotification('Contact info created successfully');
                }
                closeModal('contactModal');
                location.reload();
            } catch (error) {
                showNotification('Error saving contact info: ' + error.message, 'error');
            }
        });
    }

    // Menu navigation
    const menuItems = document.querySelectorAll('.menu-item');
    const sections = document.querySelectorAll('.admin-section');
    
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            
            menuItems.forEach(mi => mi.classList.remove('active'));
            sections.forEach(section => section.classList.remove('active'));
            
            this.classList.add('active');
            
            const sectionId = this.getAttribute('data-section') + '-section';
            document.getElementById(sectionId).classList.add('active');
        });
    });
});

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// ═══════════════════════════════════════════════════════════════
//  DRAG-AND-DROP ROW REORDERING  (mouse events, maximally simple)
// ═══════════════════════════════════════════════════════════════
(function () {
    const REORDER_URLS = {
        projects:       '/api/projects/reorder',
        skills:         '/api/skills/reorder',
        education:      '/api/education/reorder',
        certifications: '/api/certifications/reorder',
        internships:    '/api/internships/reorder',
    };

    const style = document.createElement('style');
    style.textContent = `
        .drag-handle { cursor: grab; color: #6c5ce7; padding: 0 8px; font-size: 15px; }
        .drag-handle i { pointer-events: none; }
        .dnd-src  { opacity: 0.4; }
        .dnd-over td { background: rgba(108,92,231,0.2) !important; }
        .dnd-ghost {
            position: fixed; z-index: 99999; pointer-events: none;
            background: #1a1a2e; border: 1.5px solid #6c5ce7;
            border-radius: 8px; padding: 7px 16px;
            color: #fff; font-size: 13px; font-family: Inter,sans-serif;
            box-shadow: 0 6px 24px rgba(108,92,231,0.5);
            white-space: nowrap; max-width: 300px;
            overflow: hidden; text-overflow: ellipsis;
        }
    `;
    document.head.appendChild(style);

    let state = null;  // { row, tbody, name, ghost }
    let overRow = null;

    /* ── mousedown on grip ─────────────────────────────── */
    document.addEventListener('mousedown', function (e) {
        const handle = e.target.closest('.drag-handle');
        if (!handle) return;
        const row   = handle.closest('tr[data-id]');
        const tbody = handle.closest('tbody.sortable-tbody');
        if (!row || !tbody) return;

        e.preventDefault();
        document.body.style.userSelect = 'none';
        document.body.style.cursor = 'grabbing';

        const cells = [...row.querySelectorAll('td')].slice(1);
        const label = cells.map(c => c.textContent.trim()).find(Boolean) || '';
        const ghost = document.createElement('div');
        ghost.className = 'dnd-ghost';
        ghost.textContent = '⠿  ' + label;
        document.body.appendChild(ghost);
        moveGhost(e.clientX, e.clientY);

        row.classList.add('dnd-src');
        state = { row, tbody, name: tbody.id.replace('-tbody',''), ghost };
    });

    /* ── mousemove ─────────────────────────────────────── */
    document.addEventListener('mousemove', function (e) {
        if (!state) return;
        moveGhost(e.clientX, e.clientY);

        if (overRow) { overRow.classList.remove('dnd-over'); overRow = null; }

        // find the tr under the cursor (skip ghost)
        state.ghost.style.display = 'none';
        const el = document.elementFromPoint(e.clientX, e.clientY);
        state.ghost.style.display = '';
        if (!el) return;

        const target = el.closest('tr[data-id]');
        if (target && target !== state.row && target.closest('tbody') === state.tbody) {
            target.classList.add('dnd-over');
            overRow = target;
        }
    });

    /* ── mouseup ───────────────────────────────────────── */
    document.addEventListener('mouseup', function (e) {
        if (!state) return;

        const target = overRow;
        const { row, tbody, name, ghost } = state;

        ghost.remove();
        row.classList.remove('dnd-src');
        if (overRow) { overRow.classList.remove('dnd-over'); overRow = null; }
        document.body.style.userSelect = '';
        document.body.style.cursor = '';
        state = null;

        if (!target || target === row) return;

        const rect  = target.getBoundingClientRect();
        const after = e.clientY > rect.top + rect.height / 2;
        tbody.insertBefore(row, after ? target.nextSibling : target);

        row.style.transition = 'background 0.5s';
        row.style.background = 'rgba(108,92,231,0.25)';
        setTimeout(() => { row.style.background = ''; row.style.transition = ''; }, 600);

        const btn = document.getElementById('save-order-' + name);
        if (btn) btn.style.display = 'inline-flex';
    });

    function moveGhost(x, y) {
        if (!state) return;
        state.ghost.style.left = (x + 16) + 'px';
        state.ghost.style.top  = (y - 10) + 'px';
    }

    /* ── Save Order ────────────────────────────────────── */
    window.saveOrder = async function (name) {
        const tbody = document.getElementById(name + '-tbody');
        if (!tbody) return;
        const rows    = [...tbody.querySelectorAll('tr[data-id]')];
        const payload = rows.map((r, i) => ({ id: parseInt(r.dataset.id, 10), order: i + 1 }));
        const btn     = document.getElementById('save-order-' + name);
        if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...'; }
        try {
            const res  = await fetch(REORDER_URLS[name], {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            if (res.ok) {
                showNotification(name.charAt(0).toUpperCase() + name.slice(1) + ' order saved!', 'success');
                if (btn) btn.style.display = 'none';
            } else {
                showNotification('Error: ' + (data.error || 'Unknown'), 'error');
            }
        } catch { showNotification('Network error.', 'error'); }
        finally {
            if (btn) { btn.disabled = false; btn.innerHTML = '<i class="fas fa-save"></i> Save Order'; }
        }
    };
})();