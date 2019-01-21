====================
Building the Website
====================

As I envision the process at the moment I will proceed by:

#. Building the Welcome Page
#. Building the Activity Page
#. Building the Section Page with it's discussion area
#. Building the Item input page.
#. Building the Item edit page.
#. Building the Item delete page.
#. Building the Comment page.
#. Building the Comment edit page.
#. Building the Comment delete page.
#. Consider adding a Response model to allow people to respond to individual comments. Build all three pages for it.

Building the Welcome Page
=========================

Overview
--------

The Welcome Page should have a paragraph explaining what the website is about and a list of the activities that are
available to date. If possible it would be nice to mark any activities that have recent entries that the current user
hasn't seen yet. That might be complicated because I would have to set some flag or find some way to know whether a user
has viewed the page. Perhaps I could start by just marking an activity when it has comments or responses more recent
than the current user's last comment or response and less than x number of days old. What should x be? Maybe 2? Maybe 5?
That may become more clear after we start using the site.

Detailed Plan
-------------

Here are the steps as I imagine them:

#. The urlpattern and WelcomeView are already in place.
#. Compose and display the explanatory paragraph at the top of a bootstrap card.
#. Display the current list of acivities under a line. Each should display it's index number and title.
#. Modify it so that it only displays activities on or after their publish date.
#. Modify it so that it does not display activities marked with archive = True.
#. Provide a means, either button or link, to get into an actual activity.

Building the Activity Page
==========================

Overview
--------

The Activity Page should display the title of the activity, present its overview and list the sections that are
currently available to the user. A section is available if it is the first section or if the user has entered at least
one comment or response on the section before. Come to think of it, all of the sections should be listed, but only the
available sections should be active, either by having a button or by being an active link itself.

A button or link at the bottom could return the user to the Welcome Page. Perhaps I could implement Previous and Next
buttons to go to the previous or next available activity.

Detailed Plan
-------------

Here are the steps as I imagine them:

#. Set the urlpattern to get to the activity summary page
#. Stub in the Activity SummaryView.
#. Stub in activity_summary.html
#. Flesh out the view.
#. Flesh out the html.

Comments
--------

I will have to return to this later. All I have done now is the listing of the sections. I also want to mark sections
with new material but that will require actually having a means to enter comments and that won't be done until later.

Building the Section Page
=========================

Overview
--------

The Section Page is where most of the action will take place. The top of the screen should give the instructions for
that Section of the Activity and the bottom portion be given over to space for discussion. Those marked as
administrators, at first just me, can post discussion items and others can add comments to those items by clicking an
Add Comment button near the item. Similarly, each comment will have a link or button next to it for anyone who wants to
add a response to that comment -- if you decide to implement responses. I suspect that may be something to save until
you find out whether it might be useful.

Each discussion point (Item) added by an administrator will be printed in bold with the comments to that discussion
point indented underneath.

Detailed Plan
-------------

Here are the steps as I imagine them:

#. Set the urlpattern to get to the section page
#. Stub in the Activity SectionView.
#. Stub in section.html
#. Flesh out the view to the point of displaying the html.
#. Flesh out the html to the point of displaying the instructions and, if present, the link.
#. Create a discussion area in the html.
#. Add the ability for the administrator(s) to add discussion points (items).
#. Add the ability for the administrator(s) to edit items they have added.
#. Add the ability for the administrator(s) to delete items they have added if no comments have yet been made.
#. Add the ability for the users to add comments to the items.
#. Add the ability for the users to edit their comments.
#. Add the ability for the users to delete their comments.


Building the Item Input Page
============================

Overview
--------

This should be a fairly simple page allowing the administrator to compose/edit a discussion point.

Detailed Plan
-------------

Whether it is really simple or not remains to be seen. I'm already re-thinking the urlpattern I had in mind for this.
Perhaps it should be something like ``activity/<a>/<s>/item/`` where <a> is the activity index and <s> is the section
index. Let's try that in the following steps.

#. Set the urlpattern and stub in the Activity ItemCreateView.
#. Stub in item_create.html.
#. Flesh out the get method of the view.
#. Flesh out the html to allow for actual input.
#. Flesh out the post method of the view.
#. Revisit section.html to adjust how the items are displayed.

Building the Item Edit Page
===========================

Overview
--------

There will be little difference between this and the Item Input page. You can probably clone create_item.html to give
you a starting point then follow what you did in Christmas2018 on the comment_edit.html page. The URL used to access it
will be ``activity/<a>/<i>/item_edit`` and that the previously composed Item should be visible in the edit box. There
should also be a Delete button here if the administrator wants to delete the Item.

Building the Item Delete Page
=============================

Overview
--------

This page will only confirm whether the administrator wants to delete the Item. If not, they go back to the Item Edit
page.

Detailed Plans
--------------

This should be a fairly close copy of what I did for deleting comments in Christmas2018. Here is a quick list of steps:

#. Update the urlpatterns to include ``activity/<a>/<i>/delete_item/`` and build the get method of ItemDeleteView.
#. Build the ``item_delete.html`` and test it out.
#. Build the post method of the ItemDeleteView.

Building the Comment Input Page
===============================

Overview
--------

This should be a fairly simple page allowing a user to compose/edit their comments for a particular discussion point. It
would be really nice if this could be in a pop-up window so they could still see the Item and/or the other comments.

Detailed Plan
-------------

I already added some "Add Comment" buttons to the end of each item section on the section page. Now I need to add a way
to actually add those comments. This page should probably end up just being a clone of item_create.html but, since the
model for a comment is different, the views will have to be different too. Here are the steps:

#. Set the urlpattern and stub in the Activity CommentCreateView.
#. Flesh out the get method of the view.
#. Copy comment_create.html from item_create.html
#. Flesh out the post method of the view.
#. Revisit section.html to adjust how the comments are displayed.

Building the Comment Edit Page
==============================

Overview
--------

This will actually be the same page as the Comment Input page, the only difference being the URL being used to access it
and that the previously composed Comment should be visible in the edit box. There should also be a Delete button here in
case the user wants to delete their Comment.

Detailed Plan
-------------

Apparently I neglected to fill out this section for the item_edit.html page. No matter, what I did for that will
work much the same here. In fact, I can probably clone the ``item_edit.html`` page as my starting point and have very
few changes to make.

#. Set the urlpattern and write the Activity CommentEditView get method.
#. Copy and edit ``comment_edit.html`` from ``item_edit.html`` and make the necessary changes.
#. Adjust the links on the ``section.html`` page.
#. Test the appearance of the comment edit page.
#. Write the post method of CommentEditView and test whether the comments really get edited.

Building the Comment Delete Page
================================

Overview
--------

This page will only confirm that the user wants to delete their Comment. If not, they go back to the Comment Edit page.

Detailed Plan
-------------

#. Set the urlpattern and write the Activity CommentDeleteView get method.
#. Copy and edit ``comment_delete.html`` from ``item_delete.html``.
#. Adjust the link on the ``section.html`` page.
#. Test the appearance of the comment delete page.
#. Write the post method of CommentDeleteView and test whether the comments really get deleted.

Thoughts on a Response Model
============================

As indicated above, it might not be worthwhile to work on this until I find out if it will really be useful or not. The
idea is to emulate a table discussion as much as possible and at table discussions people should not get off into side
conversations.

The Mail App
============

Overview
--------

I think I can pretty much copy and paste this whole thing from Christmas2018, though I will have to make some changes to
be sure that Sylvia gets copied whenever I send an e-mail to a minor. With exactly two minors I think I can just put a
new function into utilities.py that checks for either Kayden or Janely's username and returns True and otherwise return
false.

Detailed Plans
--------------

#. Do a python manage.py startapp mail.
#. Copy the templates folder, urls.py and views.py from Chrismas2018.
#. Add the mail app to INSTALLED_APPS.
#. Add is_minor to utilities.py
#. Add the mail app to config.urls.py
#.
