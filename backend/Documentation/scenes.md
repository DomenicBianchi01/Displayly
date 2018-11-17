**There is a Postman collection in this folder that you can use to test all of the endpoints**

------
Scenes
------

**1. Create A New Scene**

Endpoint: `POST http://131.104.48.82:5000/workspaces/{workspaceId}/scenes`

`workspaceId`: The ID of the workspace you wish to add a scene to.

In the body, you must include the following properties: Name (the name of the scene).

```
{
	"name": "Name of scene"
}
```

In order to access this endpoint, you must include the JWT token in the `Authorization` header of the network request. Only users who have access to the specified `workspaceId` will be able to add displays to it

If created successfully, the following will be returned:

```
{
	"success": true,
	"sceneId": #
}
```

**2. Get List Of Scenes In Workspace**

Endpoint: `GET http://131.104.48.82:5000/workspaces/{workspaceId}/scenes`

There is no body required, instead, to get a list of scenes belonging to a workspace, you specify the Workspace ID directly in the URL. For example, if I wanted to see the list of scenes for a workspace with ID 1: `GET http://131.104.48.82:5000/workspaces/1/scenes`.

In order to access this endpoint, you must include the JWT token in the `Authorization` header of the network request. Only users who have access to the specified `workspaceId` will be able to access its scenes.

A sample response would look like:

```
{
    "success": true,
    "scenes": [
        {
            "id": 1,
            "name": "A scene",
	    "slides": []
        },
        {
            "id": 2,
            "name": "Another scene",
	    "slides": [1, 2, 3]
        }
    ]
}
```

* `id`: A unique identifier for the scene.
* `name`: The name of the scene. This is not unique.
* `slides`: An array of slides that are assigned to the scene (the groups of slides that will be shown on a display when the scene is being displayed on a display)

**3. Assign Slides To A Scene**

Endpoint: `PUT http://131.104.48.82:5000/workspaces/{workspaceId}/scenes/{sceneId}`

You can assign multiple slides to a scene. To do so, in the body of the request, provide an array of slide ID's:

```
{
	"slides": [1, 2, 3]
}
```

To remove all slides from the scene:

```
{
	"slides": []
}
```

If changed successfully, a `200` status code will be returned. Otherwise, `400` or `401` with an error message.

In order to access this endpoint, you must include the JWT token in the `Authorization` header of the network request. Only users who have access to the specified `workspaceId` will be able to modify its scenes.

**4. Delete A Scene**

Endpoint: `DELETE http://131.104.48.82:5000/workspaces/{workspaceId}/scenes/{sceneId}`

No body is needed, just include the `sceneId` and the `workspaceId` that the scene belongs to in the URL.

In order to access this endpoint, you must include the JWT token in the `Authorization` header of the network request. Only users who have access to the specified `workspaceId` will be able to modify its scenes.

**IMPORTANT:** If a Display is currently displaying the scene you are trying to delete, the request will be rejected. You must unassign the scene from the display first.