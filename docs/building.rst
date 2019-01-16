====================
Building the Website
====================

As I envision the process at the moment I will proceed by:

#. Building the Welcome Page
#. Building the Activity Page
#. Build the Section Page with it's discussion area
#. Build the Item input page.
#. Build the Item edit page.
#. Build the Item delete page.
#. Build the Comment page.
#. Build the Comment edit page.
#. Build the Comment delete page.
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

Building the Item Input Page
============================

Overview
--------

This should be a fairly simple page allowing the administrator to compose/edit a discussion point.

Building the Item Edit Page
===========================

Overview
--------

This will actually be the same page as the Item Input page, the only difference being the URL being used to access it
and that the previously composed Item should be visible in the edit box. There should also be a Delete button here if
the administrator wants to delete the Item.

Building the Item Delete Page
=============================

Overview
--------

This page will only confirm that the administrator wants to delete the Item. If not, they go back to the Item Edit page.

Building the Comment Input Page
===============================

Overview
--------

This should be a fairly simple page allowing a user to compose/edit their comments for a particular discussion point. It
would be really nice if this could be in a pop-up window so they could still see the Item and/or the other comments.

Building the Comment Edit Page
==============================

Overview
--------

This will actually be the same page as the Comment Input page, the only difference being the URL being used to access it
and that the previously composed Comment should be visible in the edit box. There should also be a Delete button here in
case the user wants to delete their Comment.

Building the Comment Delete Page
================================

Overview
--------

This page will only confirm that the user wants to delete their Comment. If not, they go back to the Comment Edit page.

Thoughts on a Response Model
============================

As indicated above, it might not be worthwhile to work on this until I find out if it will really be useful or not. The
idea is to emulate a table discussion as much as possible and at table discussions people should not get off into side
conversations.
