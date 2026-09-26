# Workaround for a Sphinx i18n bug: the ``Locale`` transform replaces
# translated nodes with freshly parsed ones but leaves the original reference
# nodes registered in ``document.refnames``.  The docutils ``TargetNotes``
# transform (used by the ``.. target-notes::`` directive in guide/index.rst)
# then iterates over those stale, detached nodes and crashes with
# ``ValueError: <reference ...> is not in list``.
#
# This extension prunes references that are no longer attached to the doctree
# just before TargetNotes runs, so translated documents build correctly.
#
# Remove this file once the underlying Sphinx issue is fixed upstream.
from docutils.transforms import Transform


class PruneStaleRefnames(Transform):
    default_priority = 539  # just before docutils TargetNotes (540)

    def apply(self):
        document = self.document
        for name, refs in list(document.refnames.items()):
            attached = [
                ref
                for ref in refs
                if ref.parent is not None and ref in ref.parent.children
            ]
            if len(attached) != len(refs):
                document.refnames[name] = attached


def setup(app):
    app.add_transform(PruneStaleRefnames)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
