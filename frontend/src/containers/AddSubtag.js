import React, { useState, useRef } from 'react'
import {
  Container,
  Grid,
  makeStyles,
  TextField,
  Button,
  Typography,
  Paper,
  Select,
} from '@material-ui/core';
import { connect } from 'react-redux'
import Editor from '../components/editor/tiny_editor/react_tiny/TinyEditorComponent';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    direction: 'ltr',
  },
  background: {
    minHeight: `calc(100vh - 5em)`,
  },
  title: {
    fontSize: 40,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    margin: 'auto',
  },
}))

const Subtag = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container justify='center' alignItems='center' className={classes.background}>
        <Grid
          xs={10}
          sm={8}
          item container
          justify='center'
          alignItems='stretch'
          direction='column'
          spacing={6}>
          <Grid item>
            <Typography gutterBottom variant='h3' className={classes.title} align='center'>
              افزودن ساب‌تگ
            </Typography>
          </Grid>
          <Grid item >
            <Paper className={classes.paper}>
              <Grid
                container
                direction='column'
                justify='center'
                spacing={2}>
                <Grid item>
                  <TextField label='عنوان' variant='outlined' gutterBottom fullWidth />
                </Grid>
                <Grid container item alignItems='center' justify='center' spacing={2}>
                  <Grid item>
                    <Select
                      variant='outlined'
                      native
                      // onChange={handleChange}
                      inputProps={{
                        name: 'age',
                        id: 'filled-age-native-simple',
                      }}
                    >
                      <option value={10}>تگ اول</option>
                      <option value={20}>تگ دوم</option>
                      <option value={30}>تگ سوم</option>
                    </Select>
                  </Grid>
                  <Grid item>
                    <Button variant='contained' color='primary'>
                      بزن بریم
                    </Button>
                  </Grid>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </Grid>
    </div>
  )
}

const mapStateToProps = (state, ownProps) => ({

})

export default connect(
  mapStateToProps,
  {

  }
)(Subtag);