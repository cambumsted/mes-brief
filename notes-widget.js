/* Send notes to Cam — shared widget (works on any page) */
(function () {
  var STORAGE_KEY = 'mes-notes-v1';
  var NAME_KEY = 'mes-notes-name';
  var RECIPIENT = 'cambumsted@microsoft.com';
  var SUBJECT = 'Marketing Effectiveness Solution';

  function load() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []; }
    catch (e) { return []; }
  }
  function save(arr) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(arr)); } catch (e) {}
  }
  function getName() { return localStorage.getItem(NAME_KEY) || ''; }
  function setName(n) { try { localStorage.setItem(NAME_KEY, n); } catch (e) {} }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function pageLabel() {
    var t = document.title || 'Page';
    return t.split('—')[0].trim() || t;
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.comment-fab')) return; // avoid double-init

    var fab = document.createElement('button');
    fab.type = 'button';
    fab.className = 'comment-fab';
    fab.innerHTML = 'Send notes to Cam <span class="badge" id="notes-badge" style="display:none">0</span>';
    document.body.appendChild(fab);

    var panel = document.createElement('div');
    panel.className = 'comment-panel hidden';
    panel.innerHTML =
      '<div class="comment-panel-header">' +
        '<h3>Notes for Cam</h3>' +
        '<button type="button" class="comment-panel-close" aria-label="Close">\u00d7</button>' +
      '</div>' +
      '<div class="comment-panel-body">' +
        '<div class="section-context">' +
          '<span class="label">Currently viewing</span>' +
          '<span class="value" id="cmt-section">\u2014</span>' +
        '</div>' +
        '<form class="note-form" autocomplete="off">' +
          '<label for="cmt-body">Add a note</label>' +
          '<textarea id="cmt-body" maxlength="2000" placeholder="What\'s on your mind?" required></textarea>' +
          '<button type="submit" class="note-add">+ Add note</button>' +
        '</form>' +
        '<div class="notes-section">' +
          '<h4><span>Your notes <span id="notes-count">(0)</span></span></h4>' +
          '<div class="notes-list" id="notes-list"></div>' +
        '</div>' +
        '<div class="send-row">' +
          '<label for="cmt-author" style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.5px;color:var(--ink-soft);font-weight:600;">Your name</label>' +
          '<input id="cmt-author" type="text" maxlength="60" placeholder="Your name" />' +
          '<button type="button" class="send-button" id="send-all" disabled>Send notes to Cam</button>' +
          '<span class="send-help">All your notes (across pages) will be bundled into a single email draft.</span>' +
          '<button type="button" class="clear-button" id="clear-all">Clear all notes</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(panel);

    var sectionEl = panel.querySelector('#cmt-section');
    var authorInput = panel.querySelector('#cmt-author');
    var bodyInput = panel.querySelector('#cmt-body');
    var form = panel.querySelector('.note-form');
    var closeBtn = panel.querySelector('.comment-panel-close');
    var listEl = panel.querySelector('#notes-list');
    var countEl = panel.querySelector('#notes-count');
    var badgeEl = document.getElementById('notes-badge');
    var sendBtn = panel.querySelector('#send-all');
    var clearBtn = panel.querySelector('#clear-all');

    authorInput.value = getName();

    function renderNotes() {
      var notes = load();
      listEl.innerHTML = '';
      notes.forEach(function (n, idx) {
        var div = document.createElement('div');
        div.className = 'note-item';
        div.innerHTML =
          '<button type="button" class="note-delete" data-idx="' + idx + '" title="Remove note">\u00d7</button>' +
          '<div class="note-section-tag">' + escapeHtml(n.section) + '</div>' +
          '<div class="note-text">' + escapeHtml(n.text) + '</div>';
        listEl.appendChild(div);
      });
      countEl.textContent = '(' + notes.length + ')';
      sendBtn.disabled = notes.length === 0;
      if (notes.length > 0) {
        badgeEl.style.display = 'inline-block';
        badgeEl.textContent = notes.length;
      } else {
        badgeEl.style.display = 'none';
      }
    }

    function updateSection() { sectionEl.textContent = pageLabel(); }

    function openPanel() {
      panel.classList.remove('hidden');
      document.body.classList.add('notes-open');
      updateSection();
      setTimeout(function () { bodyInput.focus(); }, 50);
    }
    function closePanel() {
      panel.classList.add('hidden');
      document.body.classList.remove('notes-open');
    }

    fab.addEventListener('click', function () {
      panel.classList.contains('hidden') ? openPanel() : closePanel();
    });
    closeBtn.addEventListener('click', closePanel);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !panel.classList.contains('hidden')) closePanel();
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var text = bodyInput.value.trim();
      if (!text) return;
      var notes = load();
      notes.push({ section: pageLabel(), text: text, ts: Date.now() });
      save(notes);
      bodyInput.value = '';
      renderNotes();
      bodyInput.focus();
    });

    listEl.addEventListener('click', function (e) {
      var btn = e.target.closest('.note-delete');
      if (!btn) return;
      var idx = parseInt(btn.getAttribute('data-idx'), 10);
      var notes = load();
      notes.splice(idx, 1);
      save(notes);
      renderNotes();
    });

    clearBtn.addEventListener('click', function () {
      var notes = load();
      if (!notes.length) return;
      if (!confirm('Clear all notes? This cannot be undone.')) return;
      save([]);
      renderNotes();
    });

    sendBtn.addEventListener('click', function () {
      var notes = load();
      if (!notes.length) return;
      var author = authorInput.value.trim();
      if (author) setName(author);

      var grouped = {};
      var order = [];
      notes.forEach(function (n) {
        if (!grouped[n.section]) { grouped[n.section] = []; order.push(n.section); }
        grouped[n.section].push(n.text);
      });

      var lines = [];
      lines.push('Notes on the Marketing Effectiveness Solution');
      lines.push('From: ' + (author || 'Anonymous'));
      lines.push('Sent: ' + new Date().toLocaleString());
      lines.push('');
      order.forEach(function (sec) {
        lines.push('=== ' + sec + ' ===');
        grouped[sec].forEach(function (t, i) { lines.push((i + 1) + '. ' + t); });
        lines.push('');
      });

      var mailto = 'mailto:' + RECIPIENT +
        '?subject=' + encodeURIComponent(SUBJECT) +
        '&body=' + encodeURIComponent(lines.join('\r\n'));
      window.location.href = mailto;
    });

    renderNotes();
  });
})();
